from __future__ import annotations

import json
import os
import shlex
import shutil
import subprocess
import threading
from contextlib import contextmanager
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from typing import Any, Iterator

import pytest


REPOSITORY = Path(__file__).resolve().parent
SKETCHY = REPOSITORY / "bin/sketchy"
SKILL = REPOSITORY / "skills/sketchy/SKILL.md"


@pytest.fixture(scope="session")
def cli_env(tmp_path_factory: pytest.TempPathFactory) -> dict[str, str]:
    uv = shutil.which("uv")
    assert uv is not None, "the Sketchy executable requires uv"

    tool_bin = tmp_path_factory.mktemp("sketchy-path")
    (tool_bin / "uv").symlink_to(Path(uv).resolve())

    env = os.environ.copy()
    env.pop("SKETCHY_URL", None)
    for name in tuple(env):
        if name.lower().endswith("_proxy"):
            env.pop(name)
    env.update(
        {
            "PATH": os.pathsep.join((str(tool_bin), "/usr/bin", "/bin")),
            "SKETCHY_TOKEN": "deterministic-test-token",
            "UV_OFFLINE": "1",
            "NO_COLOR": "1",
            "COLUMNS": "240",
            "NO_PROXY": "127.0.0.1,localhost",
        }
    )
    return env


def run_sketchy(
    cli_env: dict[str, str],
    *args: str,
    site: str | None = None,
    executable: Path = Path("bin/sketchy"),
) -> subprocess.CompletedProcess[bytes]:
    command = [str(executable)]
    if site is not None:
        command.extend(("--site", site))
    command.extend(args)
    return subprocess.run(
        command,
        cwd=REPOSITORY,
        env=cli_env,
        capture_output=True,
        check=False,
        timeout=60,
    )


def portable_path(path: Path) -> str:
    resolved = str(path.resolve())
    home = str(Path.home())
    if resolved.startswith(f"{home}/"):
        relative = resolved[len(home) + 1 :]
        return f"~/{shlex.quote(relative)}"
    return shlex.quote(resolved)


@contextmanager
def sketchy_server(
    responses: dict[tuple[str, str], tuple[int, Any]],
) -> Iterator[tuple[str, list[dict[str, Any]]]]:
    requests: list[dict[str, Any]] = []

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self) -> None:
            self.respond()

        def do_POST(self) -> None:
            self.respond()

        def do_PATCH(self) -> None:
            self.respond()

        def do_DELETE(self) -> None:
            self.respond()

        def respond(self) -> None:
            request: dict[str, Any] = {
                "method": self.command,
                "path": self.path,
                "authorization": self.headers.get("Authorization", ""),
            }
            content_length = int(self.headers.get("Content-Length", "0"))
            if content_length:
                body = self.rfile.read(content_length)
                content_type = self.headers.get("Content-Type", "")
                request["content_type"] = content_type
                request["body"] = body
                if content_type == "application/json":
                    request["json"] = json.loads(body)
            requests.append(request)
            status, payload = responses.get(
                (self.command, self.path),
                (500, {"detail": f"Unexpected request: {self.command} {self.path}"}),
            )
            body = json.dumps(payload).encode()
            self.send_response(status)
            self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body)))
            self.end_headers()
            self.wfile.write(body)

        def log_message(self, format: str, *args: object) -> None:
            pass

    server = ThreadingHTTPServer(("127.0.0.1", 0), Handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        host, port = server.server_address
        yield f"http://{host}:{port}", requests
    finally:
        server.shutdown()
        server.server_close()
        thread.join()


def test_list_is_compact_by_default_full_is_complete_and_hints_use_this_executable(
    cli_env: dict[str, str],
) -> None:
    payload = {
        "count": 1,
        "sketches": [
            {
                "slug": "orbit",
                "title": "Orbit",
                "sketch_type": "d3",
                "updated_at": "2026-07-24T12:00:00Z",
                "startup_js": "drawOrbit()",
                "div_html": '<div id="orbit"></div>',
                "owner": {"id": 7, "username": "artist"},
                "revision": 3,
            }
        ],
    }
    route = ("GET", "/sketchy/api/sketches/")

    with sketchy_server({route: (200, payload)}) as (site, requests):
        compact = run_sketchy(cli_env, "list", site=site)
        full = run_sketchy(cli_env, "list", "--full", site=site)

    assert compact.returncode == 0
    assert full.returncode == 0
    assert compact.stdout and not compact.stdout.endswith(b"\n")
    assert full.stdout and not full.stdout.endswith(b"\n")

    assert b"slug,title,sketch_type,updated_at" in compact.stdout
    assert b"startup_js" not in compact.stdout
    assert b"div_html" not in compact.stdout
    assert b"owner_username" not in compact.stdout
    assert b"revision" not in compact.stdout

    assert b"startup_js" in full.stdout
    assert b"div_html" in full.stdout
    assert b"owner_id" in full.stdout
    assert b"owner_username" in full.stdout
    assert b"revision" in full.stdout

    hint = f"Run `{portable_path(SKETCHY)} --site {shlex.quote(site)} list --full` to see complete API fields."
    assert hint.encode() in compact.stdout
    assert requests == [
        {
            "method": "GET",
            "path": "/sketchy/api/sketches/",
            "authorization": "Bearer deterministic-test-token",
        },
        {
            "method": "GET",
            "path": "/sketchy/api/sketches/",
            "authorization": "Bearer deterministic-test-token",
        },
    ]


def test_delete_404_is_a_successful_noop_but_get_404_is_an_error(
    cli_env: dict[str, str],
) -> None:
    route = "/sketchy/api/sketches/missing/"
    responses = {
        ("DELETE", route): (404, {"detail": "Sketch not found."}),
        ("GET", route): (404, {"detail": "Sketch not found."}),
    }

    with sketchy_server(responses) as (site, requests):
        deleted = run_sketchy(cli_env, "delete", "missing", site=site)
        fetched = run_sketchy(cli_env, "get", "missing", site=site)

    assert deleted.returncode == 0
    assert b"already absent; no-op" in deleted.stdout
    assert deleted.stdout and not deleted.stdout.endswith(b"\n")

    assert fetched.returncode == 1
    assert b"Sketch not found." in fetched.stdout
    assert b"status: 404" in fetched.stdout
    assert [request["method"] for request in requests] == ["DELETE", "GET"]


def test_mutation_commands_send_json_and_multipart_and_map_http_errors(
    cli_env: dict[str, str], tmp_path: Path
) -> None:
    media_id = "123e4567-e89b-12d3-a456-426614174000"
    responses = {
        ("POST", "/sketchy/api/sketches/"): (
            201,
            {"sketch": {"slug": "orbit", "title": "Orbit", "sketch_type": "d3"}},
        ),
        ("PATCH", "/sketchy/api/sketches/orbit%20draft/"): (
            409,
            {"detail": "That slug is already in use."},
        ),
        ("POST", "/sketchy/api/media/"): (
            201,
            {"media": {"id": media_id, "original_name": "texture.png"}},
        ),
    }
    upload = tmp_path / "texture.png"
    upload.write_bytes(b"\x89PNG\r\nsketchy-test")

    with sketchy_server(responses) as (site, requests):
        created = run_sketchy(
            cli_env,
            "create",
            "--slug",
            "orbit",
            "--title",
            "Orbit",
            "--type",
            "d3",
            "--startup-js",
            "drawOrbit()",
            site=site,
        )
        updated = run_sketchy(
            cli_env,
            "update",
            "orbit draft",
            "--new-slug",
            "orbit",
            "--title",
            "Revised Orbit",
            site=site,
        )
        uploaded = run_sketchy(
            cli_env,
            "media",
            "upload",
            str(upload),
            "--sketch",
            "orbit",
            "--expires-in-hours",
            "24",
            site=site,
        )

    assert created.returncode == 0
    assert updated.returncode == 1
    assert b"That slug is already in use." in updated.stdout
    assert b"status: 409" in updated.stdout
    assert uploaded.returncode == 0
    assert f"sketchy-media://{media_id}".encode() in uploaded.stdout

    assert requests[0]["path"] == "/sketchy/api/sketches/"
    assert requests[0]["json"] == {
        "slug": "orbit",
        "title": "Orbit",
        "sketch_type": "d3",
        "startup_js": "drawOrbit()",
    }
    assert requests[1]["path"] == "/sketchy/api/sketches/orbit%20draft/"
    assert requests[1]["json"] == {
        "slug": "orbit",
        "title": "Revised Orbit",
    }
    assert requests[2]["path"] == "/sketchy/api/media/"
    assert requests[2]["content_type"].startswith("multipart/form-data; boundary=")
    multipart_body = requests[2]["body"]
    assert b'name="sketch"\r\n\r\norbit' in multipart_body
    assert b'name="expires_in_hours"\r\n\r\n24' in multipart_body
    assert b'name="file"; filename="texture.png"' in multipart_body
    assert b"Content-Type: image/png" in multipart_body
    assert b"\x89PNG\r\nsketchy-test" in multipart_body
    assert all(
        request["authorization"] == "Bearer deterministic-test-token"
        for request in requests
    )


def test_create_help_keeps_each_example_on_its_own_line(
    cli_env: dict[str, str],
) -> None:
    result = run_sketchy(cli_env, "create", "--help")

    assert result.returncode == 0
    lines = {line.strip() for line in result.stdout.decode().splitlines()}
    assert {
        'sketchy create --slug orbit --title "Orbit" --type d3 --startup-js-file orbit.js',
        "sketchy create --slug canvas --title \"Canvas\" --type raw --div-html '<canvas></canvas>'",
        'sketchy create --slug demo --title "Demo" --type processing --startup-js-file demo.js --div-html-file demo.html',
    } <= lines


def test_skill_output_is_byte_equal_to_the_committed_skill(
    cli_env: dict[str, str],
) -> None:
    result = run_sketchy(cli_env, "skill")

    assert result.returncode == 0
    assert result.stdout == SKILL.read_bytes()


def test_skill_check_accepts_current_content_and_rejects_an_isolated_stale_copy(
    cli_env: dict[str, str], tmp_path: Path
) -> None:
    current = run_sketchy(cli_env, "skill", "--check")

    assert current.returncode == 0
    assert b"status: current" in current.stdout
    assert current.stdout and not current.stdout.endswith(b"\n")

    copied_executable = tmp_path / "bin/sketchy"
    copied_skill = tmp_path / "skills/sketchy/SKILL.md"
    copied_executable.parent.mkdir(parents=True)
    copied_skill.parent.mkdir(parents=True)
    shutil.copy2(SKETCHY, copied_executable)
    copied_skill.write_bytes(SKILL.read_bytes() + b"\n# stale test copy\n")

    stale = run_sketchy(
        cli_env,
        "skill",
        "--check",
        executable=copied_executable,
    )

    assert stale.returncode == 1
    assert b"The committed Sketchy skill is stale." in stale.stdout
    assert b"type: skill_check" in stale.stdout

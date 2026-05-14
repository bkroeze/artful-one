"""Compile TypeScript sketches to JavaScript files."""

from pathlib import Path

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Compile TypeScript sketches to JavaScript files"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Delete existing compiled JS files before compiling",
        )
        parser.add_argument(
            "--watch",
            action="store_true",
            help="Watch for file changes and recompile",
        )

    def handle(self, *args, **options):
        # Settings
        from django.conf import settings

        sketches_dir = Path(settings.BASE_DIR) / "sketches" / "art"
        static_dir = Path(settings.BASE_DIR) / "static" / "art"
        lib_dir = sketches_dir / "lib"
        clear = options.get("clear", False)
        watch = options.get("watch", False)

        self.stdout.write(f"Sketches directory: {sketches_dir}")
        self.stdout.write(f"Static/output directory: {static_dir}")
        self.stdout.write(f"Library directory: {lib_dir}")

        if clear:
            self.clear_compiled_files(static_dir)

        # Find all TypeScript files to compile
        ts_files = [
            f
            for f in sketches_dir.rglob("*.ts")
            if "lib" not in f.parts
            and "node_modules" not in f.parts
            and not f.name.endswith(".d.ts")
        ]

        if not ts_files:
            self.stdout.write(self.style.WARNING("No TypeScript sketch files found"))
            return

        self.stdout.write(f"Found {len(ts_files)} sketch(es) to compile")
        compiled = 0

        for ts_file in ts_files:
            slug = ts_file.stem
            js_file = static_dir / f"{slug}.js"

            # Check if JS needs rebuilding
            if js_file.exists() and not clear:
                ts_mtime = ts_file.stat().st_mtime
                js_mtime = js_file.stat().st_mtime
                if ts_mtime <= js_mtime:
                    self.stdout.write(f"  Skipping {slug} (already up to date)")
                    continue

            # Compile using esbuild
            if self.compile_sketch(ts_file, js_file):
                compiled += 1
                self.stdout.write(f"  Compiled {slug}")
            else:
                self.stdout.write(self.style.ERROR(f"  Failed to compile {slug}"))

        self.stdout.write(
            self.style.SUCCESS(f"\nDone! Compiled {compiled} sketch(es).")
        )
        if watch:
            self.stdout.write("\nWatch mode not fully implemented yet.")
            # For watch mode, we would use watchdog library here

    def clear_compiled_files(self, static_dir):
        """Delete all compiled JS files."""
        if not static_dir.exists():
            return
        for js_file in static_dir.glob("*.js"):
            self.stdout.write(f"  Deleting {js_file.name}")
            js_file.unlink()
        if static_dir.exists() and not any(static_dir.iterdir()):
            # Only remove directory if empty
            static_dir.rmdir()

    def compile_sketch(self, ts_file, js_file):
        """Compile a single TypeScript file to JavaScript using esbuild."""
        try:
            from subprocess import check_output, CalledProcessError
        except ImportError:
            self.stdout.write(self.style.ERROR("subprocess module not available"))
            return False

        # Ensure output directory exists
        js_file.parent.mkdir(parents=True, exist_ok=True)

        # Build esbuild command
        cmd = [
            "npx",
            "-y",
            "esbuild",
            str(ts_file),
            "--bundle",
            "--target=es2020",
            "--format=iife",
            f"--outfile={js_file}",
            "--external:p5",
        ]

        try:
            check_output(cmd, timeout=30)
            return True
        except CalledProcessError as e:
            self.stdout.write(self.style.ERROR(f"  Error: {e}"))
            return False
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"  Error: {e}"))
            return False

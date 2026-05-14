from unittest import mock

from django.test import TestCase  # type: ignore[import-untyped]
from django.template.loader import render_to_string  # type: ignore[import-untyped]
from django.urls import reverse  # type: ignore[import-untyped]


class RpgChargenPageTests(TestCase):
    def test_supers_page_includes_shared_htmx_script(self):
        response = self.client.get(reverse("rpg_chargen:supers"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "includes/htmx.html")
        self.assertContains(response, "https://unpkg.com/htmx.org@1.9.12")
        self.assertTemplateUsed(
            response, "rpg_chargen/partials/botanical_spider_loader.html"
        )
        self.assertTemplateUsed(response, "rpg_chargen/partials/robot_web_loader.html")
        self.assertContains(response, "data-spider-loader")
        self.assertContains(response, "data-robot-loader")
        self.assertContains(response, 'hx-target="#names-results-panel"')
        self.assertContains(response, 'id="character-details-panel"')
        self.assertContains(response, 'id="supers-generator-form"')
        self.assertContains(response, "data-copy-markdown")
        self.assertNotContains(response, 'id="startBtn"')
        self.assertNotContains(response, 'id="stopBtn"')
        self.assertNotContains(response, 'id="resetBtn"')
        self.assertNotContains(response, 'id="toggleRobot"')
        self.assertNotContains(response, 'id="speakNow"')

    def test_icons_page_includes_shared_htmx_script(self):
        response = self.client.get(reverse("rpg_chargen:icons"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "includes/htmx.html")
        self.assertContains(response, "https://unpkg.com/htmx.org@1.9.12")

    def test_character_rows_use_hidden_inputs_for_detail_generation(self):
        rendered = render_to_string(
            "rpg_chargen/partials/characters_table.html",
            {
                "genre": 'Dark "Gritty"',
                "characters": [
                    {
                        "name": 'Quote "Hero"',
                        "tagline": "Protects & serves",
                        "description": 'Says "yes" before trouble arrives',
                    }
                ],
            },
        )

        self.assertIn('hx-include="closest tr"', rendered)
        self.assertNotIn("hx-vals", rendered)
        self.assertIn('data-copy-markdown="#generated-names-markdown"', rendered)
        self.assertIn('hx-include="#supers-generator-form"', rendered)
        self.assertIn('aria-label="Retry name generation"', rendered)
        self.assertIn('name="character_name" value="Quote &quot;Hero&quot;"', rendered)
        self.assertIn('name="tagline" value="Protects &amp; serves"', rendered)
        self.assertIn(
            'name="description" value="Says &quot;yes&quot; before trouble arrives"',
            rendered,
        )

    def test_character_details_success_includes_copy_and_retry_controls(self):
        rendered = render_to_string(
            "rpg_chargen/partials/character_details.html",
            {
                "genre": "Superhero",
                "character": {
                    "name": "Moon Loom",
                    "tagline": "Weaves moonlight",
                    "description": "A nocturnal defender",
                    "origin": "Lunar loom accident",
                },
            },
        )

        self.assertIn('data-copy-markdown="#character-details-markdown"', rendered)
        self.assertIn('aria-label="Retry detail generation"', rendered)
        self.assertIn('hx-include="#character-details-retry-values"', rendered)
        self.assertIn('name="character_name" value="Moon Loom"', rendered)
        self.assertIn("## Moon Loom", rendered)

    @mock.patch("rpg_chargen.views.NameGenerator.generate_with_llm")
    def test_generate_names_llm_failure_returns_clean_error(self, generate_mock):
        generate_mock.side_effect = RuntimeError(
            "OpenRouter rejected key sk-secret-example"
        )

        with self.assertLogs("rpg_chargen.views", level="ERROR") as logs:
            response = self.client.post(
                reverse("rpg_chargen:generate_names"),
                {"num_names": "3", "genre": "Superhero"},
                HTTP_HX_REQUEST="true",
            )

        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Could not generate names", content)
        self.assertIn("Error reference:", content)
        self.assertNotIn("sk-secret-example", content)
        self.assertIn("RPG chargen name generation failed", "\n".join(logs.output))
        self.assertNotIn("sk-secret-example", "\n".join(logs.output))
        self.assertIn("exception_type=RuntimeError", "\n".join(logs.output))

    @mock.patch("rpg_chargen.views.CharacterGenerator.generate")
    def test_generate_details_llm_failure_returns_clean_error(self, generate_mock):
        generate_mock.side_effect = TimeoutError("provider timeout after 30s")

        with self.assertLogs("rpg_chargen.views", level="ERROR") as logs:
            response = self.client.post(
                reverse("rpg_chargen:generate_details"),
                {
                    "character_name": "Moon Loom",
                    "tagline": "Weaves moonlight",
                    "description": "A nocturnal defender",
                    "genre": "Superhero",
                },
                HTTP_HX_REQUEST="true",
            )

        content = response.content.decode()
        self.assertEqual(response.status_code, 200)
        self.assertIn("Could not generate character details", content)
        self.assertIn("Error reference:", content)
        self.assertNotIn("provider timeout after 30s", content)
        self.assertIn(
            "RPG chargen character detail generation failed", "\n".join(logs.output)
        )
        self.assertNotIn("provider timeout after 30s", "\n".join(logs.output))
        self.assertIn("exception_type=TimeoutError", "\n".join(logs.output))

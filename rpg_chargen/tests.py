
from django.test import TestCase
from django.urls import reverse


class RpgChargenPageTests(TestCase):
    def test_supers_page_includes_shared_htmx_script(self):
        response = self.client.get(reverse("rpg_chargen:supers"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "includes/htmx.html")
        self.assertContains(response, "https://unpkg.com/htmx.org@1.9.12")

    def test_icons_page_includes_shared_htmx_script(self):
        response = self.client.get(reverse("rpg_chargen:icons"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "includes/htmx.html")
        self.assertContains(response, "https://unpkg.com/htmx.org@1.9.12")

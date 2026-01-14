"""Tests for RPG app views and templates."""

import json

from django.test import TestCase, Client
from django.urls import reverse

from rpg.models import RpgTable, RpgTableAlias


class RpgNamesPageTestCase(TestCase):
    """Test the RPG names page and table rendering."""

    def setUp(self):
        self.client = Client()

    def test_table_dropdown_renders_without_null(self):
        """Test that table dropdown options don't render 'null' in HTML.

        This tests the fix for aod-e6d4 where tables with None/empty addons
        were rendering with 'null' in the data-addons attribute.
        """
        # Create a test table with addons
        table_with_addons = RpgTable.objects.create(
            slug="names/test-with-addons",
            description="Test Table With Addons",
            variant="columns",
            delimiter=" ",
            data=[["foo", "bar"], ["baz", "qux"]],
            hidden=False,
            addon={"DEFAULT": "2.3", "epithets": "2.3"},
        )
        for alias in ["test.with.addons", "test"]:
            RpgTableAlias.objects.create(alias=alias, table=table_with_addons)

        # Create a test table without addons
        table_without_addons = RpgTable.objects.create(
            slug="names/test-without-addons",
            description="Test Table Without Addons",
            variant="columns",
            delimiter="",
            data=[["alpha", "beta"]],
            hidden=False,
            addon=None,
        )
        RpgTableAlias.objects.create(alias="test.no.addons", table=table_without_addons)

        # Make request to the names page
        response = self.client.get(reverse("rpg:names"))

        # Check page loads successfully
        self.assertEqual(response.status_code, 200)

        content = response.content.decode("utf-8")

        # Test: The word "null" should NOT appear in the option tags without addons
        # For table without addons, the data-addons attribute should be empty or ""
        self.assertIn(f'value="{table_without_addons.slug}"', content)
        # The data-addons attribute should either not be present or be empty, not "null"
        # Check that 'data-addons="null"' does not appear in content
        self.assertNotIn(
            'data-addons="null"',
            content,
            "Found 'data-addons=\"null\"' in HTML response",
        )

        # For table with addons at least, verify data-addons is set properly
        self.assertIn(f'value="{table_with_addons.slug}"', content)

        # The response should contain JSON for addons table, not just "null"
        # For a table with addons, the data-addons should be a JSON object
        # Let's check that the addon description appears
        self.assertIn(table_with_addons.description, content)


class RpgTemplateFiltersTestCase(TestCase):
    """Custom template filter tests."""

    def test_to_json_filter_with_none(self):
        """Test to_json filter with None value."""
        from rpg.templatetags.rpg_filters import to_json

        result = to_json(None)
        self.assertEqual(result, "")

    def test_to_json_filter_with_dict(self):
        """Test to_json filter with dict value."""
        from rpg.templatetags.rpg_filters import to_json

        value = {"DEFAULT": "2.3", "epithets": "2.3"}
        result = to_json(value)

        # Should be valid JSON
        parsed = json.loads(result)
        self.assertEqual(parsed, value)

    def test_to_json_filter_with_empty_dict(self):
        """Test to_json filter with empty dict."""
        from rpg.templatetags.rpg_filters import to_json

        result = to_json({})
        self.assertEqual(result, "{}")

    def test_to_json_filter_with_list(self):
        """Test to_json filter with list value."""
        from rpg.templatetags.rpg_filters import to_json

        value = ["foo", "bar", "baz"]
        result = to_json(value)

        parsed = json.loads(result)
        self.assertEqual(parsed, value)


class RpgHtmxEndpointsTestCase(TestCase):
    """Test HTMX endpoints."""

    def setUp(self):
        self.client = Client()
        # Create test table
        self.table = RpgTable.objects.create(
            slug="test/simple",
            description="Simple Test Table",
            variant="columns",
            delimiter=" ",
            data=[["foo", "bar"], ["baz", "qux"]],
            hidden=False,
        )
        RpgTableAlias.objects.create(alias="test.simple", table=self.table)

    def test_htmx_generate_post_returns_200(self):
        """Test that POST to /rpg/names/generate returns 200 (not 403).

        This tests the fix for aod-cbb6 where the endpoint was returning 403
        due to missing csrf_exempt decorator.
        """
        response = self.client.post(
            reverse("rpg:htmx_generate"),
            {"table": "test.simple", "count": 5},
        )
        # Should return 200, not 403
        self.assertEqual(response.status_code, 200)

        content = response.content.decode("utf-8")
        # Check that we got the names table HTML back
        self.assertIn("ui celled table", content)

    def test_htmx_generate_generates_names(self):
        """Test that generate endpoint actually generates names."""
        response = self.client.post(
            reverse("rpg:htmx_generate"),
            {"table": "test.simple", "count": 3},
        )
        self.assertEqual(response.status_code, 200)

        content = response.content.decode("utf-8")
        # Should have a table with generated names
        self.assertIn('class="ui celled table"', content)
        self.assertIn("Name", content)

    def test_htmx_generate_with_addon(self):
        """Test generate with addon parameter."""
        response = self.client.post(
            reverse("rpg:htmx_generate"),
            {"table": "test.simple", "count": 2, "addon": "test"},
        )
        # Should still work even if addon doesn't exist for this table
        self.assertEqual(response.status_code, 200)

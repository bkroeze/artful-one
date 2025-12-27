import datetime
import json
import uuid
import xml.etree.ElementTree as ET

import pytest
from django.utils import timezone
from django.utils.text import slugify

from blog.models import PreviousTagName, Tag
from blog.templatetags.entry_tags import do_typography_string

from .factories import BlogmarkFactory, EntryFactory, NoteFactory, QuotationFactory


@pytest.mark.django_db(transaction=True)
class TestBlog:
    def test_homepage(self, client):
        db_entries = [
            EntryFactory(),
            EntryFactory(),
            EntryFactory(),
        ]
        BlogmarkFactory()
        QuotationFactory()
        NoteFactory()
        response = client.get("/")
        entries = response.context["entries"]
        assert [e.pk for e in entries] == [
            e.pk for e in sorted(db_entries, key=lambda e: e.created, reverse=True)
        ]

    def test_other_pages(self, client):
        entry = EntryFactory()
        blogmark = BlogmarkFactory()
        quotation = QuotationFactory()
        note = NoteFactory()
        for path in (
            "/",
            "/{}/".format(entry.created.year),
            entry.get_absolute_url(),
            blogmark.get_absolute_url(),
            quotation.get_absolute_url(),
            note.get_absolute_url(),
            "/{}/".format(entry.created.year),
            "/atom/everything/",
        ):
            response = client.get(path)
            assert response.status_code == 200

    def test_entry(self, client):
        entry = EntryFactory()
        response = client.get(entry.get_absolute_url())
        assert "entry.html" in [template.name for template in response.templates]
        assert response.context["entry"].pk == entry.pk

    def test_blogmark(self, client):
        blogmark = BlogmarkFactory()
        response = client.get(blogmark.get_absolute_url())
        assert "blogmark.html" in [template.name for template in response.templates]
        assert response.context["blogmark"].pk == blogmark.pk

    def test_quotation(self, client):
        quotation = QuotationFactory()
        response = client.get(quotation.get_absolute_url())
        assert "quotation.html" in [template.name for template in response.templates]
        assert response.context["quotation"].pk == quotation.pk

    def test_note(self, client):
        note = NoteFactory()
        response = client.get(note.get_absolute_url())
        assert "note.html" in [template.name for template in response.templates]
        assert response.context["note"].pk == note.pk

    def test_cache_header_for_old_content(self, client):
        old_date = timezone.now() - datetime.timedelta(days=181)
        entry = EntryFactory(created=old_date)
        response = client.get(entry.get_absolute_url())
        assert response.headers["cache-control"] == "s-maxage=%d" % (24 * 60 * 60)

    def test_no_cache_header_for_recent_content(self, client):
        recent_entry = EntryFactory(created=timezone.now())
        response = client.get(recent_entry.get_absolute_url())
        assert "cache-control" not in response.headers

    def test_archive_year(self, client):
        quotation = QuotationFactory()
        response = client.get("/{}/".format(quotation.created.year))
        assert response.status_code == 200
        assert "archive_year.html" in [template.name for template in response.templates]

    def test_markup(self, client):
        entry = EntryFactory(
            title="Hello & goodbye",
            body="<p>First paragraph</p><p>Second paragraph</p>",
        )
        response = client.get(entry.get_absolute_url())
        decoded_content = response.content.decode()
        assert "Hello &amp; goodbye" in decoded_content
        assert "<p>First paragraph</p><p>Second paragraph</p>" in decoded_content

    def test_update_blogmark_runs_commit_hooks(self):
        # This was throwing errors on upgrade Django 2.2 to 2.2.1
        blogmark = BlogmarkFactory()
        assert blogmark.pk
        blogmark.commentary = "hello there"
        blogmark.save()

    def test_do_typography_string(self):
        for input, expected in (
            ("Hello, world", "Hello, world"),
            ('Hello, "world"!', "Hello, “world”!"),
            ("Hello, world's!", "Hello, world’s!"),
            ('Hello, <"world"!', "Hello, <“world”!"),
            # Do not do these ones:
            ('Hello, <"world">!', 'Hello, <"world">!'),
            ("Hello, <'world'>!", "Hello, <'world'>!"),
            # This caused a recursion error at one point
            (
                """Should you pin your library's dependencies using "click>=7,<8" or "click~=7.0"? Henry Schreiner's short answer is no, and his long answer is an exhaustive essay covering every conceivable aspect of this thorny Python packaging problem.""",
                'Should you pin your library\'s dependencies using "click>=7,<8" or "click~=7.0"? Henry Schreiner\'s short answer is no, and his long answer is an exhaustive essay covering every conceivable aspect of this thorny Python packaging problem.',
            ),
        ):
            assert do_typography_string(input) == expected

    def test_rename_tag_creates_previous_tag_name(self, client):
        tag = Tag.objects.create(tag="old-name")
        tag.entry_set.create(
            title="Test entry",
            body="Test entry body",
            created="2020-01-01T00:00:00+00:00",
        )
        assert client.get("/tags/old-name/").status_code == 200
        assert client.get("/tags/new-name/").status_code == 404
        tag.rename_tag("new-name")
        assert tag.tag == "new-name"
        previous_tag_name = PreviousTagName.objects.get(tag=tag)
        assert previous_tag_name.previous_name == "old-name"
        assert client.get("/tags/old-name/").status_code == 301
        assert client.get("/tags/new-name/").status_code == 200

    def test_tag_with_hyphen(self):
        tag = Tag.objects.create(tag="tag-with-hyphen")
        assert tag.tag == "tag-with-hyphen"

    def test_draft_items_not_displayed(self, client):
        draft_entry = EntryFactory(is_draft=True, title="draftentry")
        draft_blogmark = BlogmarkFactory(is_draft=True, link_title="draftblogmark")
        draft_quotation = QuotationFactory(is_draft=True, source="draftquotation")
        draft_note = NoteFactory(is_draft=True, body="draftnote")
        random_slug = slugify(f"testing-{uuid.uuid4()}")
        testing = Tag.objects.get_or_create(tag=random_slug)[0]

        live_entry = EntryFactory(title="publishedentry", created=draft_entry.created)
        live_blogmark = BlogmarkFactory(
            link_title="publishedblogmark", created=draft_blogmark.created
        )
        live_quotation = QuotationFactory(
            source="publishedquotation", created=draft_quotation.created
        )
        live_note = NoteFactory(body="publishednote", created=draft_note.created)

        for obj in (
            draft_entry,
            draft_blogmark,
            draft_quotation,
            draft_note,
            live_entry,
            live_blogmark,
            live_quotation,
            live_note,
        ):
            obj.tags.add(testing)

        paths = (
            "/",  # Homepage
            "/{}/".format(draft_entry.created.year),
            "/{}/{}/".format(
                draft_entry.created.year, draft_entry.created.strftime("%b")
            ),
            "/{}/{}/{}/".format(
                draft_entry.created.year,
                draft_entry.created.strftime("%b"),
                draft_entry.created.day,
            ),
            f"/search/?q={random_slug}",
            f"/tags/{random_slug}/",
            live_entry.get_absolute_url(),
        )

        counts = json.loads(client.get(f"/tags-autocomplete/?q={random_slug}").content)
        assert counts == {
            "tags": [
                {
                    "id": 1,
                    "tag": random_slug,
                    "description": "",
                    "total_entry": 1,
                    "total_blogmark": 1,
                    "total_quotation": 1,
                    "total_note": 1,
                    "is_exact_match": 1,
                    "count": 4,
                }
            ]
        }

        for path in paths:
            response = client.get(path)
            assert "draftentry" not in response.content.decode()

        robots_fragment = '<meta name="robots" content="noindex">'
        draft_warning_fragment = "This is a draft post"

        for obj in (draft_entry, draft_blogmark, draft_quotation, draft_note):
            response2 = client.get(obj.get_absolute_url())
            content = response2.content.decode()
            assert robots_fragment in content
            assert draft_warning_fragment in content
            assert (
                response2.headers["cache-control"]
                == "private, no-cache, no-store, must-revalidate"
            )

            # Publish it
            obj.is_draft = False
            obj.save()

            response3 = client.get(obj.get_absolute_url())
            content = response3.content.decode()
            assert robots_fragment not in content
            assert draft_warning_fragment not in content
            assert "cache-control" not in response3.headers

        counts2 = json.loads(client.get(f"/tags-autocomplete/?q={random_slug}").content)
        assert counts2 == {
            "tags": [
                {
                    "id": 1,
                    "tag": random_slug,
                    "description": "",
                    "total_entry": 2,
                    "total_blogmark": 2,
                    "total_quotation": 2,
                    "total_note": 2,
                    "is_exact_match": 1,
                    "count": 8,
                }
            ]
        }

        for path in paths:
            response4 = client.get(path)
            assert "draftentry" in response4.content.decode()

    def test_draft_items_not_in_feeds(self, client):
        draft_entry = EntryFactory(is_draft=True, title="draftentry")
        draft_blogmark = BlogmarkFactory(is_draft=True, link_title="draftblogmark")
        draft_quotation = QuotationFactory(is_draft=True, source="draftquotation")

        response1 = client.get("/atom/entries/")
        assert draft_entry.title not in response1.content.decode()

        response2 = client.get("/atom/links/")
        assert draft_blogmark.link_title not in response2.content.decode()

        response3 = client.get("/atom/everything/")
        assert draft_entry.title not in response3.content.decode()
        assert draft_blogmark.link_title not in response3.content.decode()
        assert draft_quotation.source not in response3.content.decode()

        # Change draft status and check they show up
        draft_entry.is_draft = False
        draft_entry.save()

        draft_blogmark.is_draft = False
        draft_blogmark.save()

        draft_quotation.is_draft = False
        draft_quotation.save()

        response4 = client.get("/atom/entries/")
        assert draft_entry.title in response4.content.decode()

        response5 = client.get("/atom/links/")
        assert draft_blogmark.link_title in response5.content.decode()

        response6 = client.get("/atom/everything/")
        assert draft_entry.title in response6.content.decode()
        assert draft_blogmark.link_title in response6.content.decode()
        assert draft_quotation.source in response6.content.decode()

    def test_entries_feed_includes_subscribe_note(self, client):
        EntryFactory()
        response = client.get("/atom/entries/")
        assert "You are only seeing the" in response.content.decode()

    def test_og_description_strips_markdown(self, client):
        blogmark = BlogmarkFactory(
            commentary="This **has** *markdown*", use_markdown=True
        )
        response = client.get(blogmark.get_absolute_url())
        content = response.content.decode()
        assert '<meta property="og:description" content="This has markdown"' in content

        note = NoteFactory(body="A note with **bold** text")
        response = client.get(note.get_absolute_url())
        content = response.content.decode()
        assert (
            '<meta property="og:description" content="A note with bold text"' in content
        )

    def test_og_description_escapes_quotes(self, client):
        blogmark = BlogmarkFactory(
            commentary='Fun new "live music model" release', use_markdown=True
        )
        response = client.get(blogmark.get_absolute_url())
        assert (
            '<meta property="og:description" content="Fun new &quot;live music model&quot; release"'
            in response.content.decode()
        )

    def test_blogmark_title_used_for_page_and_feed(self, client):
        blogmark_with_title = BlogmarkFactory(
            link_title="Link Title", title="Custom Title"
        )
        blogmark_without_title = BlogmarkFactory(link_title="Another Link")

        # Page title uses custom title if provided
        response = client.get(blogmark_with_title.get_absolute_url())
        assert "<title>Custom Title</title>" in response.content.decode()

        response2 = client.get(blogmark_without_title.get_absolute_url())
        assert "<title>Another Link</title>" in response2.content.decode()

        # Atom feeds use title if present otherwise link_title
        feed_response = client.get("/atom/links/")
        root = ET.fromstring(feed_response.content)
        ns = {"atom": "http://www.w3.org/2005/Atom"}
        titles = [e.find("atom:title", ns).text for e in root.findall("atom:entry", ns)]
        assert "Custom Title" in titles
        assert "Another Link" in titles
        assert "Link Title" not in titles

        feed_response2 = client.get("/atom/everything/")
        root2 = ET.fromstring(feed_response2.content)
        titles2 = [
            e.find("atom:title", ns).text for e in root2.findall("atom:entry", ns)
        ]
        assert "Custom Title" in titles2
        assert "Another Link" in titles2
        assert "Link Title" not in titles2

    def test_og_description_escapes_quotes_entry(self, client):
        entry = EntryFactory(body='<p>Entry with "quotes" in it</p>')
        response = client.get(entry.get_absolute_url())
        assert (
            '<meta property="og:description" content="Entry with “quotes” in it"'
            in response.content.decode()
        )

    def test_og_description_escapes_quotes_note(self, client):
        note = NoteFactory(body='Note with "quotes" inside')
        response = client.get(note.get_absolute_url())
        assert (
            '<meta property="og:description" content="Note with &quot;quotes&quot; inside"'
            in response.content.decode()
        )

    def test_og_description_escapes_quotes_quotation(self, client):
        quotation = QuotationFactory(quotation='A "quoted" statement', source="Someone")
        response = client.get(quotation.get_absolute_url())
        assert (
            '<meta property="og:description" content="A &quot;quoted&quot; statement"'
            in response.content.decode()
        )

    def test_og_description_escapes_quotes_tag_page(self, client):
        tag = Tag.objects.create(tag="test", description='Tag with "quotes"')
        entry = EntryFactory()
        entry.tags.add(tag)
        response = client.get("/tags/test/")
        content = response.content.decode()
        import re

        # Match curly single quotes around 'test' and allow for both straight or curly single quotes
        assert re.search(
            r'<meta property="og:description" content="1 posts tagged [\u2018\u2019\']test[\u2018\u2019\']',
            content,
        )

    def test_top_tags_page(self, client):
        for i in range(1, 12):
            tag = Tag.objects.create(tag=f"tag{i}")
            for j in range(i):
                entry = EntryFactory(title=f"Entry{i}-{j}")
                entry.tags.add(tag)
        response = client.get("/top-tags/")
        assert response.status_code == 200
        tags_info = response.context["tags_info"]
        assert len(tags_info) == 10
        assert tags_info[0]["tag"].tag == "tag11"
        assert not any(info["tag"].tag == "tag1" for info in tags_info)
        latest = Tag.objects.get(tag="tag11").entry_set.order_by("-created")[0].title
        assert latest in response.content.decode()

    def test_search_title_displays_full_month_name(self, client):
        tag = Tag.objects.create(tag="llm-release")
        entry = EntryFactory(
            created=datetime.datetime(2025, 7, 1, tzinfo=datetime.timezone.utc)
        )
        entry.tags.add(tag)
        response = client.get("/search/?tag=llm-release&year=2025&month=7")
        assert "Posts tagged llm-release in July, 2025" in response.content.decode()

    def test_archive_month_shows_search_and_counts(self, client):
        created = datetime.datetime(2025, 7, 1, tzinfo=datetime.timezone.utc)
        EntryFactory(created=created)
        EntryFactory(created=created)
        BlogmarkFactory(created=created)
        QuotationFactory(created=created)
        response = client.get("/2025/Jul/")
        assert response.status_code == 200
        assert (
            '<input type="hidden" name="year" value="2025">'
            in response.content.decode()
        )
        assert (
            '<input type="hidden" name="month" value="7">' in response.content.decode()
        )
        assert "4 posts:" in response.content.decode()
        assert ">2 entries</a>" in response.content.decode()
        assert ">1 link</a>" in response.content.decode()
        assert ">1 quote</a>" in response.content.decode()
        assert "/search/?type=entry&year=2025&month=7" in response.content.decode()
        assert "/search/?type=blogmark&year=2025&month=7" in response.content.decode()
        assert "/search/?type=quotation&year=2025&month=7" in response.content.decode()
        summary = response.content.decode()
        assert "note" not in summary

    def test_archive_month_includes_notes(self, client):
        created = datetime.datetime(2025, 7, 1, tzinfo=datetime.timezone.utc)
        # Add an entry outside July 2025 so the calendar works
        EntryFactory(
            created=datetime.datetime(2024, 1, 1, tzinfo=datetime.timezone.utc)
        )
        NoteFactory(created=created)
        QuotationFactory(created=created)
        BlogmarkFactory(created=created)
        response = client.get("/2025/Jul/")
        assert response.status_code == 200
        assert "3 posts:" in response.content.decode()
        assert ">1 note</a>" in response.content.decode()
        assert "/search/?type=note&year=2025&month=7" in response.content.decode()

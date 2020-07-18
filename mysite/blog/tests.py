from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from blog.views import cv_page, cvpost_new


class CVPageTest(TestCase):

    def test_root_url_resolves_to_cv_page_view(self):
        found = resolve('/cv/')
        self.assertEqual(found.func, cv_page)

    def test_cv_page_returns_correct_html(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<div class="cv">', html)
        self.assertTrue(html.endswith('</html>'))

    def test_cv_page_returns_correct_title(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<title>Anandbir\'s Website</title>', html)

    def test_post_edit_contains_title_field_and_text_field(self):
        request = HttpRequest()
        response = cvpost_new(request)
        html = response.content.decode('utf8')
        self.assertIn('id="id_title"', html)
        self.assertIn('id="id_text"', html)

    def test_cv_page_contains_a_eduction_section(self):
        request = HttpRequest()
        response = cv_page(request)
        html = response.content.decode('utf8')
        self.assertIn('<h4>EDUCATION</h4>', html)


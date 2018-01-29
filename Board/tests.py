from django.test import TestCase
from django.urls import reverse,resolve

from .views import home

class HomeTests(TestCase):
    def text_home_view_code(self):
        url = reverse()
        response = self.client.get(url)
        self.assertEqual(response.status_code == '200')

    def test_home_url_resolved_home_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home)


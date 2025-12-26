from django.test import TestCase
from django.urls import reverse


class HomeRedirectTests(TestCase):
    def test_home_redirects_to_sales(self):
        resp = self.client.get('/')
        self.assertEqual(resp.status_code, 302)
        self.assertEqual(resp['Location'], reverse('perfume-list'))

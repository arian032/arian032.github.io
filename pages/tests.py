from django.test import TestCase
from django.shortcuts import reverse


class PageTest(TestCase):

    def test_home_page_by_url(self):
        response = self.client.get('')
        return self.assertEqual(response.status_code, 200)

    def test_home_page_by_url_name(self):
        response = self.client.get(reverse('home'))
        return self.assertEqual(response.status_code, 200)

    def test_aboutus_page_by_url(self):
        response = self.client.get('/about_us/')
        return self.assertEqual(response.status_code, 200)

    def test_aboutus_page_by_url_name(self):
        response = self.client.get(reverse('about_us'))
        return self.assertEqual(response.status_code, 200)

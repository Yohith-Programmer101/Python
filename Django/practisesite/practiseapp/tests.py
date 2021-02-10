from django.test import TestCase

class test_all_pages(TestCase):
    def test_all_pages(self):
        all_pages = ['', '/viewname', '/createname', '/login', '/loggedin', '/list', '/classbased']

        for i in all_pages:
            url = (i)
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
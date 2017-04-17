from django.test import TestCase

from lists.views import home_page


class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        request = self.client.get('/')
        response = home_page(request)
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

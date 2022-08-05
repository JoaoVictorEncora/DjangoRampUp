from django.test import TestCase


class ViewTests(TestCase):
    def test_show_loads_properly(self, ):
        response = self.client.get('http://127.0.0.1:8000/show')
        self.assertEqual(response.status_code, 200)

    def test_emp_loads_properly(self, ):
        response = self.client.get('http://127.0.0.1:8000/emp')
        self.assertEqual(response.status_code, 200)

from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class ViewsTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_view(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(response.status_code, 200)
        # Check status code 200 or not

    def test_logout_view(self):
        response = self.client.get(reverse('logout'))
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

    def test_register_view(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)

    def test_register_post(self):
        # Assuming your register view expects a POST request with form data
        data = {'username': 'testuser', 'password1': 'testpassword', 'password2': 'testpassword'}
        response = self.client.post(reverse('register'), data)
        self.assertEqual(response.status_code, 302)  # Expecting a redirect

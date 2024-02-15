from django.test import TestCase
from django.contrib.auth.models import User
from ..form import CreateUserForm  # Replace 'your_app' with the actual name of your Django app


class CreateUserFormTest(TestCase):
    def test_valid_form(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_blank_data(self):
        form = CreateUserForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['username'], ['This field is required.'])
        self.assertEqual(form.errors['password1'], ['This field is required.'])
        self.assertEqual(form.errors['password2'], ['This field is required.'])

    def test_passwords_not_matching(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'password1': 'testpassword123',
            'password2': 'differentpassword',
        }
        form = CreateUserForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['password2'], ['The two password fields didn’t match.'])

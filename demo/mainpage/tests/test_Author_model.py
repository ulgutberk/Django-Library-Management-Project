from django.test import TestCase
from ..models import Authors


class AuthorsModelTest(TestCase):
    def test_create_author(self):
        author = Authors.objects.create(name='John', surname='Doe', biography='A fictional author')
        self.assertEqual(author.name, 'John')
        self.assertEqual(author.surname, 'Doe')
        self.assertEqual(author.biography, 'A fictional author')
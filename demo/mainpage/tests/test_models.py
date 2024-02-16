from django.test import TestCase
from ..models import Authors, Books


class AuthorsModelTest(TestCase):
    def test_create_author(self):
        author = Authors.objects.create(name='John', surname='Doe', biography='A fictional author')
        self.assertEqual(author.name, 'John')
        self.assertEqual(author.surname, 'Doe')
        self.assertEqual(author.biography, 'A fictional author')


class BooksModelTest(TestCase):
    def setUp(self):
        # Create an author for testing
        self.author = Authors.objects.create(name='Test Name', surname='Test Surname', biography='Test biography')

    def test_create_book(self):
        book = Books.objects.create(
            title='Test Book',
            author=self.author,
            publisher='Test Publisher',
            pages=200,
            publish_date='2024-02-15'
        )

        self.assertEqual(book.title, 'Test Book')
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.publisher, 'Test Publisher')
        self.assertEqual(book.pages, 200)
        self.assertEqual(book.stock, 1)  # Default value
        self.assertEqual(book.available, True)  # Default value
        self.assertEqual(book.publish_date, '2024-02-15')  # Blank=True, null=True

    def test_str_method(self):
        book = Books.objects.create(
            title='Test Book',
            author=self.author,
            publisher='Test Publisher',
            pages=200,
            publish_date='2024-02-15'
        )
        self.assertEqual(str(book.title), 'Test Book')
        self.assertEqual(str(book.author), 'Test Name Test Surname')
        self.assertEqual(str(book.publisher), 'Test Publisher')
        self.assertEqual(book.pages, 200)
        self.assertEqual(book.stock, 1)
        self.assertEqual(book.available, True)
        self.assertEqual(str(book.publish_date), '2024-02-15')



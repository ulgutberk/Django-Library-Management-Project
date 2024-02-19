from django.test import TestCase
from django.utils import timezone
from ..models import Authors, Books


class BooksModelTest(TestCase):
    def setUp(self):
        # Create an example author
        self.author = Authors.objects.create(name='Test Name', surname='Test Surname', biography='Example Biography')

    def test_book_creation(self):
        # Create a book
        book = Books.objects.create(
            title='Sample Book',
            author=self.author,
            publisher='Example Publisher',
            pages=200,
            stock=10,
            available=True,
            publish_date=timezone.now()
        )

        # Check if the book is created successfully
        self.assertEqual(book.title, 'Sample Book')
        self.assertEqual(book.author, self.author)
        self.assertEqual(book.publisher, 'Example Publisher')
        self.assertEqual(book.pages, 200)
        self.assertEqual(book.stock, 10)
        self.assertTrue(book.available)
        self.assertIsNotNone(book.publish_date)

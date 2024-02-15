from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from ..models import Authors, Books
from ..api.serializers import AuthorsSerializer, BookSerializer
from ..api.views import (
    AuthorsListCreateAPIView,
    AuthorsDetailAPIView,
    BooksListCreateAPIView,
    BookDetailAPIView,
)


class AuthorsListCreateAPIViewTest(TestCase):
    def setUp(self):
        self.url = reverse('author-list')
        self.client = APIClient()

    def test_author_list_create_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed for your specific case


class AuthorsDetailAPIViewTest(TestCase):
    def setUp(self):
        # Provide values for required fields
        self.author = Authors.objects.create(name='Test Author', surname='Test Surname')
        self.url = reverse('author-detail', args=[self.author.id])
        self.client = APIClient()

    def test_author_detail_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BooksListCreateAPIViewTest(TestCase):
    def setUp(self):
        self.url = reverse('books-list')
        self.client = APIClient()

    def test_books_list_create_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests as needed for your specific case


class BookDetailAPIViewTest(TestCase):
    def setUp(self):
        # Provide values for required fields
        self.book = Books.objects.create(title='Test Book', pages=100, publish_date='2020-05-22', author=Authors.objects.create(name='Test', surname='Test'))
        self.url = reverse('books-detail', args=[self.book.id])
        self.client = APIClient()

    def test_book_detail_api_view(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..api.views import AuthorsListCreateAPIView, AuthorsDetailAPIView, BooksListCreateAPIView, BookDetailAPIView


class TestUrls(SimpleTestCase):
    def test_author_list_url_is_resolved(self):
        url = reverse('author-list')
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(AuthorsListCreateAPIView.as_view()))

    def test_author_detail_url_is_resolved(self):
        url = reverse('author-detail', args=[1])
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(AuthorsDetailAPIView.as_view()))

    def test_books_list_url_is_resolved(self):
        url = reverse('books-list')
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(BooksListCreateAPIView.as_view()))

    def test_books_detail_url_is_resolved(self):
        url = reverse('books-detail', args=[1])
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(BookDetailAPIView.as_view()))

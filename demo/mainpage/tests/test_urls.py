from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..api.views import AuthorsListCreateAPIView, AuthorsDetailAPIView, BooksListCreateAPIView, BookDetailAPIView


# class TestUrls(SimpleTestCase):
#
#     def test_list_uls_is_resolved(self):
#         assert 1 == 2
# #(.venv) PS C:\Users\b84347451\PycharmProjects\demoProject\demo> python manage.py test mainpage
# Found 1 test(s).
# System check identified no issues (0 silenced).
# F
# ======================================================================
# FAIL: test_list_uls_is_resolved (mainpage.tests.test_urls.TestUrls.test_list_uls_is_resolved)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "C:\Users\b84347451\PycharmProjects\demoProject\demo\mainpage\tests\test_urls.py", line 7, in test_list_uls_is_resolved
#     assert 1 == 2
# AssertionError

class TestUrls(SimpleTestCase):
    def test_author_list_url_is_resolved(self):
        url = reverse('author-list')
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(AuthorsListCreateAPIView.as_view()))

    def test_author_detail_url_is_resolved(self):
        url = reverse('author-detail',  args=[1])
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(AuthorsDetailAPIView.as_view()))

    def test_books_list_url_is_resolved(self):
        url = reverse('books-list')
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(BooksListCreateAPIView.as_view()))

    def test_books_detail_url_is_resolved(self):
        url = reverse('books-detail',  args=[1])
        resolved_func = resolve(url).func
        print(resolved_func)
        self.assertIsInstance(resolved_func, type(BookDetailAPIView.as_view()))

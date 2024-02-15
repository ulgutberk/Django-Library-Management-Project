from django.urls import path
from . import views as api_views

# Concrete Views
urlpatterns = [
    path('authors/', api_views.AuthorsListCreateAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', api_views.AuthorsDetailAPIView.as_view(), name='author-detail'),
    path('books/', api_views.BooksListCreateAPIView.as_view(), name='books-list'),
    path('books/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='books-detail'),
]

# Generic Based
# urlpatterns = [
#     path('authors-list/', api_views.AuthorsListCreateAPIView.as_view(), name='author-list'),
# ]
# as_view ile Class i View e cevirdik

# Class Based
# urlpatterns = [
#     path('authors-list/', api_views.AuthorsListCreateAPIView.as_view(), name='author-list'),
#     # path('books-list/', api_views.BooksListCreateAPIView.as_view(), name='books-list'),
#     # path('books-detail/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='books-detail')
# ]

# Function Based
# urlpatterns = [
#     path('books-list/', api_views.book_list_api_view, name='book-list'),
#     path('books-create/', api_views.book_create_api_view, name='book-create'),
#     path('books-detail/<int:pk>/', api_views.books_detail_api_view, name='books-detail')
# ]

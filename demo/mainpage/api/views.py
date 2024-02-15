from ..models import Books, Authors
from .serializers import BookSerializer, AuthorsSerializer

# Concrete Views
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework import permissions
# We could add permissions with this library
from .permissions import IsAdminUserOrReadOnly
# Add new Custom Permission
from .pagination import SmallPagination, LargePagination
# Pagination Settings

# Generic Views
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.mixins import ListModelMixin, CreateModelMixin

# Class Views
from rest_framework.response import Response


# We use Response instead of Render, Redirect

# from rest_framework.views import APIView
# from rest_framework import status

# Function Views
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view


# Concrete Views
# -------------------------------------------------------------
class AuthorsListCreateAPIView(generics.ListCreateAPIView):
    queryset = Authors.objects.all().order_by('id')
    serializer_class = AuthorsSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = SmallPagination


class AuthorsDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Authors.objects.all()
    serializer_class = AuthorsSerializer
    permission_classes = [IsAdminUserOrReadOnly]


class BooksListCreateAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all().order_by('id') # With order_by(id) --> Listed in ascending order by id number
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]
    pagination_class = LargePagination

    # def perform_create(self, serializer):  # Override the perform_create
    #     # path('books/<int:pk>/', api_views.BookDetailAPIView.as_view(), name='books-detail'),
    #     author_pk = self.kwargs['pk']  # # Retrieve author_pk from the URL
    #     author = get_object_or_404(Books, pk=author_pk)  # Retrieve the corresponding author or return 404
    #     serializer.save(author)  # Save the book instance with the associated author
    #


class BookDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUserOrReadOnly]

# GenericAPI View based API Views
# -------------------------------------------------------------
# class AuthorsListCreateAPIView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     serializer_class = AuthorsSerializer  # Define Serializer
#     queryset = Authors.objects.all()  # Get all Authors
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# Class based API Views
# -------------------------------------------------------------
# class AuthorsListCreateAPIView(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             books = Authors.objects.all()
#             serializer = AuthorsSerializer(books, many=True)  # many=True means We sent many Query Set to Serializer
#             return Response(serializer.data)
#
#     def post(self, request):
#         serializer = AuthorsSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BooksListCreateAPIView(APIView):
#     def get(self, request):
#         if request.method == 'GET':
#             books = Books.objects.filter(available=True)
#             serializer = BookSerializer(books, many=True)
#             return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data, many=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# class BookDetailAPIView(APIView):
#     def get_object(self, pk):
#         book = get_object_or_404(Books, pk=pk)
#         return book
#
#     def get(self, request, pk):
#         book = self.get_object(pk=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         book = self.get_object(pk=pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data, status=status.HTTP_200_OK
#             )
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         book = self.get_object(pk=pk)
#         book.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

# Function Based Views
# -------------------------------------------------------------
# @api_view(['GET'])  # We use GET request bcz of we list data
# def book_list_api_view(request):
#     if request.method == 'GET':
#         books = Books.objects.filter(available=True)  # Return Query Set. Bcz of that we use many=True
#         serializer = BookSerializer(books, many=True)  # many=True means We sent many Query Set to Serializer
#         return Response(serializer.data)
#
#
# @api_view(['POST'])
# def book_create_api_view(request):
#     serializer = BookSerializer(data=request.data, many=True)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# book-detail ile pk uzerinden PUT ve DELETE methodlari eklendigi icin bunlara gerek kalmamistir.
# @api_view(['PUT'])
# def book_update_api_view(request, pk):
#     book = Books.objects.get(id=pk)
#     if request.method == 'PUT':
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(
#                 serializer.data, status=status.HTTP_200_OK
#             )
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['DELETE'])
# def book_delete_api_view(request, pk):
#     book = Books.objects.get(id=pk)
#     if request.method == 'DELETE':
#         book.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )


# @api_view(['GET', 'PUT', 'DELETE'])
# def books_detail_api_view(request, pk):
#     try:
#         books = Books.objects.get(pk=pk)
#     except Books.DoesNotExist:
#         return Response(
#             {
#                 'error': {
#                     'code': 404,
#                     'message': f'For {pk}, Book not found'
#                 }
#             },
#             status=status.HTTP_404_NOT_FOUND
#         )
#     if request.method == 'GET':
#         serializer = BookSerializer(books)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == 'PUT':
#         serializer = BookSerializer(books, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         books.delete()
#         return Response(
#             status=status.HTTP_204_NO_CONTENT
#         )

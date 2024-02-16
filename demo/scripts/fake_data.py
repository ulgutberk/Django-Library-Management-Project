import os
import random
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

import django

django.setup()

# ///////////////////////////////////////////////////////////////////////////
from mainpage.api.serializers import BookSerializer, AuthorsSerializer
from django.contrib.auth.models import User
from faker import Faker
import requests
from mainpage.models import Authors, Books
from django.db.models import Q
from pprint import pprint

# /////////////////////////////////////////////////////


fake = Faker('en_US')  # Define Faker base lang.


# Fake User Creator
def create_user(max_user=5):
    counter = 0
    while counter < max_user:
        # Create Fake User
        f_name = fake.first_name()
        l_name = fake.last_name()

        u_name = f'{f_name.title()}{l_name.lower()}'
        f_email = f'{u_name}@{fake.domain_name()}'

        user_check = User.objects.filter(username=u_name)
        while user_check.exists():
            u_name = u_name + str(random.randint(1, 100))
            user_check = User.objects.filter(username=u_name)

        user = User(
            username=u_name,
            first_name=f_name,
            last_name=l_name,
            email=f_email,
        )
        user.set_password('testpass')
        user.save()
        counter += 1
        print(f'Created user: {u_name}, Email: {f_email}')


# python .\manage.py shell_plus

# from scripts.fake_data import create_user

# from django.contrib.auth.models import User

# create_user()


def book_add(subject, max_books=10):
    fake = Faker('en_US')
    url = 'http://openlibrary.org/search.json?'
    payload = {'q': subject}
    print('Requesting  data')
    response = requests.get(url, params=payload)  # With Response, We request the JSON from endpoint
    if response.status_code != 200:
        print('Invalid response', response.status_code)
        return None

    jsn_data = response.json()  # Change the data to JSON format
    books = jsn_data.get('docs')  # Get docs in JSON data

    counter = 0

    for book in books:
        if counter > max_books:
            break

        # Extract author information
        name_parts = book.get('author_name')[0].split()
        first_name = name_parts[0] if name_parts else ''
        last_name = ' '.join(name_parts[1:]) if len(name_parts) > 1 else ' '
        print(name_parts)

        # Check if the author already exists
        author_object = Authors.objects.filter(Q(name=first_name) & Q(surname=last_name)).first()
        if author_object:
            # Use the existing author
            print('Existing Author')
            # Create a new author
        else:  # If Author data don`t exists create new one
            author_data = {
                'name': first_name,
                'surname': last_name,
                'biography': fake.text(max_nb_chars=100)
            }

            print(f'Adding Author. Author_data={author_data}')
            print(type(author_data))

            serializer_author = AuthorsSerializer(data=author_data)
            print('Serializing Author Data')

            if serializer_author.is_valid():
                serializer_author.save()
                print('Author added:', author_data)
                author_object = Authors.objects.filter(Q(name=first_name) & Q(surname=last_name)).first()
            else:
                print('Error creating author:', serializer_author.errors)
                continue  # Skip to the next iteration if author creation fails

        # Create book data
        # book_title = book.get('title')
        # book_pub = book.get('publisher')
        book_data = {
            'title': book.get('title'),
            'author': author_object.id,
            'publisher': book.get('publisher')[0],
            'pages': book.get('number_of_pages_median'),
            'stock': str(random.randint(1, 100)),
            'available': fake.boolean(chance_of_getting_true=80),
            'publish_date': fake.date_between(start_date='-30y', end_date='now').strftime('%Y-%m-%d')
        }
        # Create and save the book

        book_object = Books.objects.filter(
            Q(title=book_data.get('title')) & Q(publisher=book_data.get('publisher'))).first()
        if book_object:
            print('Existing Book')
        else:
            serializer_book = BookSerializer(data=book_data)
            print('Serializing Book Data')
            if serializer_book.is_valid():
                try:
                    print('Book Data is valid')
                    serializer_book.save()
                    print('Book added:', book_data.get('title'))
                except:
                    print('Error Book didnt added', serializer_book.errors)

            else:
                print('Error creating book:', serializer_book.errors)

        # Increment the counter
        counter += 1

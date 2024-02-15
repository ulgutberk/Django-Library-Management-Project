from rest_framework import serializers
from ..models import Books, Authors
from datetime import datetime, date
from django.utils.timesince import timesince


class BookSerializer(serializers.ModelSerializer):
    time_since_pub = serializers.SerializerMethodField()

    # Created a new func for time_since_pub it does not storage in db but sent with Serializer

    # author = serializers.StringRelatedField()

    # author = AuthorsSerializer()

    # To see Author names on JSON

    class Meta:
        model = Books
        fields = '__all__'
        # fields = ['id', 'title', 'author']
        # Specify field names

        # exclude = ['publish_date']
        # Exclude publish_date

        read_only_fields = ['id']

    def validate(self, data):  # Object level validation
        if data.get('stock') < 0:
            raise serializers.ValidationError('Stock must be greater than 0')
        elif data.get('pages') < 0:
            raise serializers.ValidationError('Page number must be greater than 0')
        return data

    def get_time_since_pub(self, object):
        # Calculate the now - publish date
        now = datetime.now()
        pub_date = object.publish_date
        time_delta = timesince(pub_date, now)
        return time_delta

    def validate_publish_date(self, datevalue):
        today = date.today()
        if datevalue > today:
            raise serializers.ValidationError('Publish date cannot be later date')
        return datevalue


class AuthorsSerializer(serializers.ModelSerializer):
    authors_books = BookSerializer(many=True, read_only=True)

    # Set many=True bcz Serializer will get many Instance
    # authors-books is related name author in Books model
    # With this structure Authors can be created without any Books
    # Used read_only= True bcz when we create a new Author we don't need to add Book.
    class Meta:
        model = Authors
        fields = '__all__'

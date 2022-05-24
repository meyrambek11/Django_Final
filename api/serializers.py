from rest_framework import serializers

from api.models import Book, Journal


class BookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'num_pages', 'genre')


class BookUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'num_pages', 'genre')


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('name', 'price', 'description', 'num_pages', 'genre')


class JournalCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'type', 'publisher')


class JournalUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'type', 'publisher')


class JournalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Journal
        fields = ('name', 'price', 'description', 'type', 'publisher')

from rest_framework import serializers
from .models import Author, Book

class BookSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(
        source='author.name',
        read_only=True
    ) 


    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'publication_year', 'author_name', 'book_cover')

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(
        many=True,
        read_only=True
    )



    class Meta:
        model = Author
        fields = ('id', 'name', 'nationality', 'books') 

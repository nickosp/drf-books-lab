from django.shortcuts import render
from rest_framework import viewsets  # <- import viewsets
from .models import Book, Author  # <- don't forget your models
from .serializers import BookSerializer, AuthorSerializer  # <- or serializers


class BookViewSet(viewsets.ModelViewSet):
        queryset = Book.objects.all()
        serializer_class = BookSerializer
        

   


class AuthorViewSet(viewsets.ModelViewSet):
        queryset = Author.objects.all()
        serializer_class = AuthorSerializer

from django.db import models
from .book import Book

class Genre(models.Model):
    name = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, related_name='genres')
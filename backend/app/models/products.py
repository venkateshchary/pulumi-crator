from django.db import models
from app.models import TimeStampedModel, Book


class Product(TimeStampedModel):
    """
    In near future we will introduce seller
    thats why we are keeping fk instead of 1-to-1
    """
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="products")
    stock = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
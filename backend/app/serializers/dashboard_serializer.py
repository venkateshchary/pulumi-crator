from rest_framework import serializers
from app.models import Product

class DashboardSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source="book.title", read_only=True)
    author_name = serializers.CharField(source="book.author.name", read_only=True)
    available=serializers.IntegerField(source="stock", read_only=True)

    class Meta:
        model= Product
        fields = ["title", "author_name", "available"]
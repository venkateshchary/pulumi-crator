from rest_framework import serializers
from app.models import Author
from .profile_serializer import ProfileSerializer

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ["id", "name"]


class AuthorProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Author
        fields = ["id", "name", "profile"] 
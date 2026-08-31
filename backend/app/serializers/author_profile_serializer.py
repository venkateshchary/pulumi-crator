from rest_framework import serializers
from .profile_serializer import ProfileSerializer
from app.models import Author


class AuthorProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()
    class Meta:
        model = Author
        fields = ["id", "name", "profile"]
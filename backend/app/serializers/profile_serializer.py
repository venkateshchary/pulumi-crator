from rest_framework import serializers
from app.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ["id", "bio"]

    def validate(self, attrs):
        if not attrs["bio"]:
            raise serializers.ValidationError("bio can't empty")

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .profile_serializer import ProfileSerializer
from .models import Profile


class ProfileView(APIView):

    def get(self, request, *args, **kwargs):
        profile_objs = Profile.objects.all()
        serialzer = ProfileSerializer(profile_objs, many=True)
        return Response(serialzer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, stats=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
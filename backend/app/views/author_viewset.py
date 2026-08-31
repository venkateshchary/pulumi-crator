# Create your views here.
from app.models import Author
from rest_framework import permissions, viewsets

from app.serializers import AuthorProfileSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = Author.objects.select_related("profile").all() # with single query
    serializer_class = AuthorProfileSerializer
    # permission_classes = [permissions.IsAuthenticated]

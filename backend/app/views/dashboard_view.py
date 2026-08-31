from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Book, Author, Product
from app.serializers import DashboardSerializer

class DashboardView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Product.objects.select_related("book__author").all()
        """
        it will do internally inner join
        """
        serializer = DashboardSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
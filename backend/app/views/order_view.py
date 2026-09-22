from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from app.models import Order
from app.serializers import OrderCreateSerializer
from django.db import transaction
import logging

logger = logging.getLogger(__name__)


class OrderView(APIView):

    def get(self, request, *args, **kwargs):
        queryset = Order.objects.all()
        serializer = OrderCreateSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = OrderCreateSerializer(data=request.data)
        if serializer.is_valid():
            with transaction.atomic():
                serializer.save()
            logger.info("returning status 201")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.info("returning status 400")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework import serializers
from app.models import OrderItem, Order, Product, OrderItem
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
import time
import logging

logger = logging.getLogger(__name__)

User = get_user_model()


class OrderItemPostSerializer(serializers.ModelSerializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["product_id", "quantity"]


class OrderCreateSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(write_only=True)
    products = OrderItemPostSerializer(many=True, write_only=True)

    class Meta:
        model = Order
        fields = ["id", "products", "created_at", "user_id"]
        read_only_fields = ["id", "created_at"]


    def validate_user_id(self, value):
        if not User.objects.filter(id=value).exists():
            raise serializers.ValidationError("User with this id doesnot exist")
        return value

    def create(self, validated_data):
        logger.info("order create is called...")
        products_data = validated_data.pop("products")
        user_id = validated_data.pop("user_id")

        user = User.objects.get(id=user_id)

        # basic order create here
        order = Order.objects.create(user=user, **validated_data)

        for item in products_data:
            logger.info(f"each item: {item}")
            try:
                product = Product.objects.select_for_update().get(id=item["product_id"])
                # logger.info("going to sleep")
                # running 100 req per without time sleep
                # each lock would hold upt to ~2ms X100 = 200 ms thinking would complete
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    {"product_id": f"Product with ID {item['product_id']} does not exist"}
                )

            # if product stock should be +ve and available for requested quantity
            if product.stock >0 and item["quantity"]<= product.stock:
                logger.info("stock is available...")
                order_obj = OrderItem(
                        order=order,
                        product=product,
                        quantity=item["quantity"],
                        price_at_purchase = product.price
                )
                order_obj.save()
                logger.info("order is saved...")
                product.stock = product.stock-item["quantity"]
                logger.info("Removing the placed item from stock count...")
                product.save()
            else:
                logger.warning("no stock is available")
                raise serializers.ValidationError(
                    {"quantity": f"Product '{product}' is out of stock or insufficient quantity available."}
                )
        return order

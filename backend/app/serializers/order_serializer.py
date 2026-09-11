from rest_framework import serializers
from app.models import OrderItem, Order, Product, OrderItem
from django.contrib.auth import get_user_model

User = get_user_model()


class OrderItemPostSerializer(serializers.ModelSerializer):
    product_id = serializers.IntergerField()
    quantity = serializers.IntegerField()

    class Meta:
        model = OrderItem
        fields = ["product_id", "quantity"]


class OrderCreateSerializer(serializers.ModelSerialzier):
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
        products_data = validated_data.pop("products")
        user_id = validated_data.pop("user_id")

        user = User.objects.get(id=user_id)
        print("validated_data: ", validated_data)

        # basic order create here
        order = Order.objects.create(user=user, **validated_data)

        order_items = []

        for item in products_data:
            try:
                product = Product.objects.get(id=item["product_id"])
            except Product.DoesNotExist:
                raise serializers.ValidationError(
                    {"product_id": f"Product with ID {item['product_id']} does not exist"}
                )

            order_items.append(
                OrderItem(
                    order=order,
                    product=product,
                    quantity=item["quantity"],
                    price_at_purchase = product.price
                )
            )
        OrderItem.objects.bulk_create(order_items)
        return order

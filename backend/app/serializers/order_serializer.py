from rest_framework import serializers

class OrderSerializer(serializers.ModelSerializer):
    product_ids = serializers.ListField(
        child= serializers.IntegerField(), # data type inside the list
        allow_empty=False
    )

    class Meta:
        pass
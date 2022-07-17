from rest_framework import serializers
from apps.mcm.models.order import Order
from apps.mcm.serializer.order_status import OrderStatusSerializer


class OrderCreateSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField(required=True)

    class Meta:
        model = Order
        read_only_fields = ["status", "created_by", "created_at"]
        exclude = ["product"]


class OrderListSerializer(serializers.ModelSerializer):

    product_id = serializers.IntegerField(source="product.id")
    created_by_user_id = serializers.IntegerField(source="created_by.id")
    status = OrderStatusSerializer()

    class Meta:
        model = Order
        exclude = ["product", "created_by"]

from rest_framework import serializers
from apps.mcm.models.order_status import OrderStatus


class OrderStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderStatus
        read_only_fields = ["created_at"]
        exclude = ["created_by"]

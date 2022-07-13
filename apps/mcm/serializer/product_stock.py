from rest_framework import serializers
from apps.mcm.serializer.user import UserSerializer
from apps.mcm.models.product_stock import ProductStock


class ProductStockSerializer(serializers.ModelSerializer):

    # created_by = UserSerializer(read_only=True)
    created_by = serializers.ReadOnlyField(source="created_by.username")
    product_name = serializers.ReadOnlyField(source="product.name")
    product_code = serializers.ReadOnlyField(source="product.code")

    class Meta:
        model = ProductStock
        fields = "__all__"
        read_only_fields = ["created_by"]
        extra_kwargs = {"product": {"write_only": True}}

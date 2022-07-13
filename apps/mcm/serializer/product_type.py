from rest_framework import serializers
from apps.mcm.serializer.user import UserSerializer
from apps.mcm.models.product_type import ProductType


class ProductTypeSerializer(serializers.ModelSerializer):

    created_by_user_name = serializers.ReadOnlyField(source="created_by.username")
    created_by_user_id = serializers.ReadOnlyField(source="created_by.id")

    class Meta:
        model = ProductType
        fields = "__all__"
        read_only_fields = ["created_by"]
        # extra_kwargs = {
        #     "created_by": {"write_only": True},
        # }

from pkg_resources import require
from rest_framework import serializers
from apps.mcm.serializer.user import UserSerializer
from apps.mcm.serializer.product_type import ProductTypeSerializer
from apps.mcm.models.product import Product
from apps.mcm.models.product_type import ProductType


class ProductCreateSerializer(serializers.ModelSerializer):

    type_id = serializers.IntegerField(required=True)

    class Meta:
        model = Product
        # fields = "__all__"
        read_only_fields = ["deleted_at", "deleted_by", "created_by", "created_at"]
        exclude = ["type"]
        # extra_kwargs = {
        #     "created_by": {"write_only": True},
        # }


class ProductListSerializer(serializers.ModelSerializer):

    type_id = serializers.IntegerField(source="type.id")

    class Meta:
        model = Product
        # fields = "__all__"
        read_only_fields = ["deleted_at", "deleted_by", "created_by"]
        exclude = ["type"]

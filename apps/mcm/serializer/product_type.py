from rest_framework import serializers
from apps.mcm.serializer.user import UserSerializer
from apps.mcm.models.product_type import ProductType


class ProductTypeSerializer(serializers.ModelSerializer):

    # highlight = serializers.HyperlinkedIdentityField(
    #     view_name="snippet-highlight", format="html"
    # )
    # created_by = serializers.ReadOnlyField(source="created_by.username")
    created_by = UserSerializer(read_only=True)
    # created_by = serializers.SlugRelatedField(many=False, read_only=True, slug_field="username")

    class Meta:
        model = ProductType
        fields = "__all__"

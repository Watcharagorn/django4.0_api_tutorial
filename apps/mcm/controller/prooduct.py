from rest_framework import permissions, viewsets, generics, mixins
from rest_framework.decorators import permission_classes
from apps.mcm.models.product import Product
from apps.mcm.serializer.product import ProductCreateSerializer, ProductListSerializer
from django.utils import timezone


class ProductViewSet(viewsets.ModelViewSet):

    queryset = Product.objects.all()
    write_serializer_class = ProductCreateSerializer
    read_serializer_class = ProductListSerializer
    permission_classes([permissions.IsAuthenticatedOrReadOnly])

    def get_serializer_class(self):
        if self.request.method == "POST":
            return self.write_serializer_class

        return self.read_serializer_class

    def perform_create(self, serializer):
        serializer.save(
            created_by=self.request.user, type_id=serializer.validated_data["type_id"]
        )

    def perform_destroy(self, instance):
        instance.created_by = self.request.user
        instance.deleted_at = timezone.now()
        instance.save()

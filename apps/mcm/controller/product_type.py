from rest_framework import permissions, viewsets
from rest_framework.decorators import permission_classes
from apps.mcm.models.product_type import ProductType
from apps.mcm.serializer.product_type import ProductTypeSerializer


class ProductTypeViewSet(viewsets.ModelViewSet):

    queryset = ProductType.objects.all()
    serializer_class = ProductTypeSerializer
    permission_classes([permissions.AllowAny])

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

from rest_framework import permissions, viewsets
from apps.mcm.management import permission
from rest_framework.decorators import permission_classes
from apps.mcm.models.product_stock import ProductStock
from apps.mcm.serializer.product_stock import ProductStockSerializer
from django.utils import timezone


class ProductStockViewSet(viewsets.ModelViewSet):

    queryset = ProductStock.objects.all()
    serializer_class = ProductStockSerializer
    permission_classes([permission.IsAdminUserOrStaff])

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

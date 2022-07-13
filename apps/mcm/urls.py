from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.mcm.controller.product_type import ProductTypeViewSet
from apps.mcm.controller.prooduct import ProductViewSet
from apps.mcm.controller.product_stock import ProductStockViewSet

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product-types")
router.register(r"product-types", ProductTypeViewSet, basename="product-types")
router.register(r"product-stock", ProductStockViewSet, basename="product-types")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.mcm.controller.product_type import ProductTypeViewSet
from apps.mcm.controller.prooduct import ProductViewSet
from apps.mcm.controller.product_stock import ProductStockViewSet
from apps.mcm.controller.order import OrderViewSet
from apps.mcm.controller.otp import send_otp

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="product")
router.register(r"product-types", ProductTypeViewSet, basename="product-types")
router.register(r"product-stock", ProductStockViewSet, basename="product-stock")
router.register(r"orders", OrderViewSet, basename="orders")
# router.register(r"orders/me", UserOrderView, basename="order-me")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
    path("otp", send_otp, name="create otp"),
]

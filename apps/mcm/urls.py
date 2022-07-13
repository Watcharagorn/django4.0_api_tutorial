from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.mcm.controller.product_type import ProductTypeViewSet

router = DefaultRouter()
router.register(r"product-types", ProductTypeViewSet, basename="product-types")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("", include(router.urls)),
]

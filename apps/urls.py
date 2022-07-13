from django.contrib import admin
from django.contrib.auth.models import User
from django.urls import include, path
from rest_framework import permissions, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from utilities.env_manager import get_environ


@api_view(["GET"])
@permission_classes([permissions.IsAuthenticatedOrReadOnly])
def HealthCheck(request):
    try:
        version, stage = get_environ()
    except Exception as identifier:
        print(identifier.__traceback__)
    finally:
        return Response({"state": stage, "version": version}, status=status.HTTP_200_OK)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path("admin/", admin.site.urls),
    path("healthcheck", HealthCheck, name="healthcheck"),
    path("api/mcm/", include("apps.mcm.urls")),
]

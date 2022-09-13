from django.contrib import admin
from django.urls import include, path, re_path
from utilities.env_manager import get_environ
from django.http import HttpResponse


def health_check(request):
    try:
        version, stage = get_environ()
    except Exception as identifier:
        print(identifier.__traceback__)
    finally:
        return HttpResponse({"state": stage, "version": version})


app_path = [path("mcm/", include("apps.mcm.urls"))]

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path("admin/", admin.site.urls),
    path("healthcheck", health_check, name="healthcheck"),
] + app_path

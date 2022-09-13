from django.urls import path
from apps.mcm.controller.otp import send_otp, async_view


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [path("otp", send_otp, name="create otp"), path("api/", async_view)]

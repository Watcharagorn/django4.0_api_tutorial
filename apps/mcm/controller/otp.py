from time import sleep
from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async
import asyncio


def sync_sleep():
    for num in range(1, 5):
        sleep(1)
        print("sleep - {}".format(num))


async def async_sleep():
    for num in range(1, 5):
        asyncio.sleep(1)
        print("sleep - {}".format(num))


## 1. function base view
# @api_view(["POST"])
# @permission_classes([permissions.AllowAny])
@csrf_exempt
async def send_otp(request):

    otp = request.data.get("otp")
    phone_number = request.data.get("phone_number")

    # setup for async
    loop = asyncio.get_event_loop()
    async_task = sync_to_async(sync_sleep, thread_sensitive=False)
    loop.create_task(async_task())

    return HttpResponse({"otp": otp, "phone_number": phone_number})

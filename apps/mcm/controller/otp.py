from time import sleep
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from asgiref.sync import sync_to_async, async_to_sync
import asyncio
import httpx


def sync_sleep():
    for num in range(1, 5):
        sleep(1)
        print("sleep - {}".format(num))


async def async_sleep():
    for num in range(1, 5):
        await asyncio.sleep(1)
        print("sleep - {}".format(num))


async def http_call_async():
    for num in range(1, 6):
        await asyncio.sleep(1)
        print(num)
    async with httpx.AsyncClient() as client:
        r = await client.get("https://httpbin.org")
        print(r)


async def async_view(request):
    loop = asyncio.get_event_loop()
    loop.create_task(http_call_async())
    return HttpResponse("Non-blocking HTTP request")


## if you need to use other annotation eg.csrf_exempt and etc.
@sync_to_async
@csrf_exempt
@async_to_sync
async def send_otp(request):

    print(request.body)

    # setup for async
    loop = asyncio.get_event_loop()
    loop.create_task(async_sleep())

    return HttpResponse(request.body)

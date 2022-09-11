from rest_framework import status, permissions
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from apps.mcm.tasks import send_otp_task
from apps.mcm.celery import error_handler, success_handler

## 1. function base view
@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def send_otp(request):

    otp = request.data.get("otp")
    phone_number = request.data.get("phone_number")
    # send_otp_task.delay(otp, phone_number)
    send_otp_task.apply_async(
        [otp, phone_number], link=[success_handler.s()], link_error=error_handler.s()
    )  # async job
    # send_otp_task.apply(
    #     [otp, phone_number], link=[success_handler.s()], link_error=error_handler.s()
    # )  # sync job
    return Response(
        {"otp": otp, "phone_number": phone_number}, status=status.HTTP_200_OK
    )

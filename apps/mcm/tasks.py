from time import sleep

from celery import shared_task
from logging import info
from win10toast import ToastNotifier


@shared_task(bind=True)
def send_otp_task(self, otp_number, phone_number):
    """Sends an email when the feedback form has been submitted."""
    sleep(5)  # Simulate expensive operation that freezes Django

    toast = ToastNotifier()
    toast.show_toast(
        "Notification",
        "Notification body",
        duration=20,
        icon_path="icon.ico",
        threaded=True,
    )
    message = "send OTP '{}' to number {}".format(otp_number, phone_number)
    info(message)
    print(message)

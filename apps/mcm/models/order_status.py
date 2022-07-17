from django.db import models


class OrderStatus(models.Model):

    STATUS = (
        ("WAIT", "WAITING FOR PAYMENT"),
        ("TRAN", "IN TRANSPORTAION"),
        ("COM", "COMPLETE"),
        ("CAN", "CANCEL"),
    )

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=300, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="order_type_created_by", on_delete=models.DO_NOTHING
    )

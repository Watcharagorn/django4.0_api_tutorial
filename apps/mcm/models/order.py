from django.db import models
from apps.mcm.models.order_status import OrderStatus
from apps.mcm.models.product import Product


class Order(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    qty = models.IntegerField()
    status = models.ForeignKey(OrderStatus, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="order_created_by", on_delete=models.DO_NOTHING
    )

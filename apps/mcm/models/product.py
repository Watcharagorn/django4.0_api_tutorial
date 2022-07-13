from django.db import models
from apps.mcm.models.product_type import ProductType


class Product(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    code = models.CharField(max_length=100)
    type = models.ForeignKey(
        ProductType, on_delete=models.DO_NOTHING, default=None, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="product_created_by", on_delete=models.DO_NOTHING
    )
    deleted_at = models.DateTimeField(default=None, null=True)
    deleted_by = models.ForeignKey(
        "auth.User",
        related_name="product_deleted_by",
        on_delete=models.DO_NOTHING,
        default=None,
        null=True,
    )

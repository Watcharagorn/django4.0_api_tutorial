from django.db import models
from apps.mcm.models.product import Product


class ProductStock(models.Model):

    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User",
        related_name="product_stock_created_by",
        on_delete=models.DO_NOTHING,
    )

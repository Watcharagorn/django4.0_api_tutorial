from django.db import models


class ProductType(models.Model):

    id = models.AutoField(primary_key=True)
    name_th = models.CharField(max_length=300)
    name_en = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="product_type_created_by", on_delete=models.DO_NOTHING
    )

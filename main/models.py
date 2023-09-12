from django.db import models
import uuid


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)
    description = models.TextField(blank=True, null=True)
    productImage = models.URLField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    sold = models.IntegerField(blank=False, null=False, default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.RESTRICT, blank=True, null=True
    )


class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Categories"

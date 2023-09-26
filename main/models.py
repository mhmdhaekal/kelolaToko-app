from django.db import models
from django.contrib.auth.models import User
import uuid


class BaseModel(models.Model):
    objects = models.Manager()

    class Meta:
        abstract = True


class Product(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False, unique=False)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField(blank=False, null=False)
    stock = models.IntegerField(blank=False, null=False)
    sold = models.IntegerField(blank=False, null=False, default=0)
    category = models.ForeignKey(
        "Category", on_delete=models.RESTRICT, blank=True, null=True
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Category(BaseModel):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255, blank=False, null=False, unique=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

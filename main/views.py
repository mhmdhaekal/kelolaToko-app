from django.shortcuts import render
from main.models import Product, Category


# Create your views here.
def index(request):
    list_all_product = Product.objects.select_related("category").values(
        "id",
        "name",
        "description",
        "productImage",
        "price",
        "stock",
        "sold",
        "category__name",
    )
    response = {
        "applicationName": "KelolaToko",
        "nama": "Muhammad Haekal Kalipaksi",
        "class": "PBP-F",
        "products": list_all_product,
    }
    return render(request, "index.html", response)

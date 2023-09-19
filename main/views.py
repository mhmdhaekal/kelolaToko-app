from django.shortcuts import render
from main.models import Product, Category
from main.forms import ProductForm, DeleteProductForm, CategoryForm, DeleteCategoryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers


# Create your views here.
def index(request):
    list_all_product = Product.objects.select_related("category").values(
        "id",
        "name",
        "description",
        "price",
        "stock",
        "sold",
        "category__name",
    )
    response = {
        "applicationName": "KelolaToko",
        "nama": "Muhammad Haekal Kalipaksi",
        "class": "PBP-F",
        "productData": {
            "count": len(list_all_product),
            "products": list_all_product,
        }
    }
    return render(request, "index.html", response)


def add_product(request):
    form = ProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "add-product.html", response)


def delete_product(request):
    form = DeleteProductForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.cleaned_data["product"]
        product.delete()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "delete-product.html", response)


def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        form.save()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "add-category.html", response)


def delete_category(request):
    form = DeleteCategoryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        category = form.cleaned_data["category"]
        category.delete()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "delete-category.html", response)


def get_product_xml(request):
    products = Product.objects.all()
    return HttpResponse(
        serializers.serialize("xml", products), content_type="application/xml"
        , status=200)


def get_product_json(request):
    products = Product.objects.all()

    return HttpResponse(
        serializers.serialize("json", products), content_type="application/json",
        status=200
    )


def get_product_by_id_xml(request, id: str):
    product = Product.objects.filter(id=id)

    return HttpResponse(
        serializers.serialize("xml", product), content_type="application/xml",
        status=200
    )


def get_product_by_id_json(request, id: str):
    product = Product.objects.filter(id=id)
    return HttpResponse(
        serializers.serialize("json", product), content_type="application/json",
        status=200
    )


def get_category_xml(request):
    categories = Category.objects.all()
    return HttpResponse(
        serializers.serialize("xml", categories), content_type="application/xml",
        status=200
    )


def get_category_json(request):
    categories = Category.objects.all()
    return HttpResponse(
        serializers.serialize("json", categories), content_type="application/json",
        status=200
    )


def get_category_by_id_xml(request, id: str):
    category = Category.objects.filter(id=id)
    return HttpResponse(
        serializers.serialize("xml", category), content_type="application/xml",
        status=200
    )


def get_category_by_id_json(request, id: str):
    category = Category.objects.filter(id=id)
    return HttpResponse(
        serializers.serialize("json", category), content_type="application/json",
        status=200
    )

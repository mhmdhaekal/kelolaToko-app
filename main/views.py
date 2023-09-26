from django.shortcuts import render
from main.models import Product, Category
from main.forms import ProductForm, DeleteProductForm, CategoryForm, DeleteCategoryForm
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.core import serializers
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
import datetime


# Create your views here.
@login_required(login_url="/login/")
def index(request):
    list_all_product = Product.objects.select_related("category").values(
        "id",
        "name",
        "description",
        "price",
        "stock",
        "sold",
        "category__name",
    ).filter(user=request.user)
    response = {
        "applicationName": "KelolaToko",
        "nama": request.user.username,
        "class": "PBP-F",
        "productData": {
            "count": len(list_all_product),
            "products": list_all_product,
        },
        "last_login" : request.COOKIES['last_login']
    }
    return render(request, "index.html", response)

@login_required(login_url="/login/")
def add_product(request):
    form = ProductForm(request.user,request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.save(commit=False)
        product.user = request.user
        product.save()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "add-product.html", response)

@login_required(login_url="/login")
def delete_product(request):
    form = DeleteProductForm(request.user ,request.POST or None)
    if form.is_valid() and request.method == "POST":
        product = form.cleaned_data["product"]
        product.delete()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "delete-product.html", response)

@login_required(login_url="/login")
def add_category(request):
    form = CategoryForm(request.POST or None)
    if form.is_valid() and request.method == "POST":
        category = form.save(commit=False)
        category.user = request.user
        category.save()
        return HttpResponseRedirect(reverse("main:index"))
    response = {"form": form}
    return render(request, "add-category.html", response)

@login_required(login_url="/login")
def delete_category(request):
    form = DeleteCategoryForm(request.user ,request.POST or None)
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

def register(request) :
    form = UserCreationForm()
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    response = {'form' : form}
    return render(request, 'register.html', response)


def login_user(request) : 
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = HttpResponseRedirect(reverse('main:index'))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response
        else:
            messages.info(request, 'Sorry, incorrect username or password. Please try again.')
            
    response = {}
    return render(request, 'login.html', response)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

@login_required(login_url="/login")
def sold_product(request):
    if (request.method == "POST"):
        product_id = request.POST.get("product_id")
        product = Product.objects.get(id=product_id)
        product.stock -= 1
        product.sold += 1
        product.save()
        return HttpResponseRedirect(reverse("main:index"))
    return HttpResponseRedirect(reverse("main:index"))
        
    
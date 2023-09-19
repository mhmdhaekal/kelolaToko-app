from django.urls import path
from main.views import index, add_product, delete_product, add_category, delete_category, get_product_xml, \
    get_product_json, get_product_by_id_xml, get_category_by_id_json, get_category_by_id_xml, get_product_by_id_json, \
    get_category_json, get_category_xml

app_name = "main"

urlpatterns = [
    path("", index, name="index"),
    path("add-product", add_product, name="add-product"),
    path("delete-product", delete_product, name="delete-product"),
    path("add-category", add_category, name="add-category"),
    path("delete-category", delete_category, name="delete-category"),
    path("get-product/xml", get_product_xml, name="get-product-xml"),
    path("get-product/json", get_product_json, name="get-product-json"),
    path("get-product/xml/<str:id>", get_product_by_id_xml, name="get-product-id-xml"),
    path("get-product/json/<str:id>", get_product_by_id_json, name="get-product-id-json"),
    path("get-category/xml", get_category_xml, name="get-category-xml"),
    path("get-category/json", get_category_json, name="get-category-json"),
    path("get-category/xml/<str:id>", get_category_by_id_xml, name="get-category-id-xml"),
    path("get-category/json/<str:id>", get_category_by_id_json, name="get-category-id-json")
]

from django.test import TestCase
from main.models import Product, Category


# Create your tests here.
class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = self.client.get("/main/")
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = self.client.get("/main/")
        self.assertTemplateUsed(response, "index.html")

    def test_products_models(self):
        product = Product.objects.create(
            name="Test Product",
            description="Test Description",
            productImage="Test Image",
            price=10000,
            stock=10,
            sold=0,
        )
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "Test Description")
        self.assertEqual(product.productImage, "Test Image")
        self.assertEqual(product.price, 10000)
        self.assertEqual(product.stock, 10)
        self.assertEqual(product.sold, 0)

    def test_category_models(self):
        category = Category.objects.create(name="Test Category")
        self.assertEqual(category.name, "Test Category")

    def test_is_my_name(self):
        response = self.client.get("/main/")
        self.assertContains(response, "Muhammad Haekal Kalipaksi")
        self.assertContains(response, "PBP-F")
        self.assertContains(response, "KelolaToko")
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
        for product in list_all_product:
            self.assertContains(response, product["name"])
            self.assertContains(response, product["description"])
            self.assertContains(response, product["productImage"])
            self.assertContains(response, product["price"])
            self.assertContains(response, product["stock"])
            self.assertContains(response, product["sold"])
            self.assertContains(response, product["category__name"])

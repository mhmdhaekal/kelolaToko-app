from django.forms import ModelForm, ModelChoiceField, ValidationError
from main.models import Product, Category


class ProductForm(ModelForm):
    category = ModelChoiceField(queryset=Category.objects.none(), to_field_name="name", required=False,
                                empty_label="null")
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)

    class Meta:
        model = Product
        fields = ["name", "description", "price", "stock", "category"]


class DeleteProductForm(ModelForm):
    product = ModelChoiceField(queryset=Product.objects.none(), to_field_name="name", required=True, empty_label=None)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['product'].queryset = Product.objects.filter(user=user)
    
    class Meta:
        model = Product
        fields = ["product"]


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class DeleteCategoryForm(ModelForm):
    category = ModelChoiceField(queryset=Category.objects.none(), to_field_name="name", required=True, empty_label=None)
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(user=user)
    
    def clean_category(self):
        category = self.cleaned_data["category"]
        if Product.objects.filter(category=category).exists():
            raise ValidationError(
                "Masih ada produk yang berada dalam kategori ini, silahkan hapus produk dan caba lagi")
        return category

    class Meta:
        model = Category
        fields = ["category"]

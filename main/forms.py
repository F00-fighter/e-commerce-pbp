from django.forms import ModelForm
from main.models import Product, Purchase

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ["name", "price","description","category","image"]

class ReviewForm(ModelForm):
    class Meta:
        model = Purchase
        fields = ['description']
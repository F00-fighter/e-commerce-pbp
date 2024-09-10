from django.shortcuts import render
from .models import Product  # Import the Product model

def show_main(request):
    products = Product.objects.all()  # Query to get all products
    return render(request, 'index.html', {'products': products})

from django.shortcuts import render
from .models import Product  # Import the Product model

def show_main(request):
    products = Product.objects.all()  # Query to get all products
    context = {
        'products': products,
        'app_name': 'Free Robux',
        'name': 'Farrel Dharmawan Dwiyudanto',
        'class': 'PBP A'
    }
    return render(request, 'index.html', context)

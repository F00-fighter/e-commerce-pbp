from django.shortcuts import render, redirect
from .models import Product  # Import the Product model
from .forms import ProductForm
from django.http import HttpResponse
from django.core import serializers

def show_main(request):
    products = Product.objects.all()  # Query to get all products
    context = {
        'products': products,
        'app_name': 'Setim',
        'name': 'Farrel Dharmawan Dwiyudanto',
        'class': 'PBP A'
    }
    return render(request, 'content.html', context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            form.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)

def show_xml(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = Product.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


def show_xml_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")


def show_json_by_id(request, id):
    data = Product.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")
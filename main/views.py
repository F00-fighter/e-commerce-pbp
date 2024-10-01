from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ReviewForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm,  AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from .models import Product, Purchase



@login_required(login_url='/login')
def show_main(request):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    products = Product.objects.all()  # Query to get all products
    last_login = request.COOKIES.get('last_login', 'Never')  # Use .get to avoid KeyError

    context = {
        'products': products,
        'user_name': user_name,
        'last_login': last_login,
    }

    return render(request, 'content.html', context)

def create_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)  # Include request.FILES for file uploads
        if form.is_valid():
            product_entry = form.save(commit=False)
            product_entry.user = request.user
            product_entry.save()
            return redirect('main:show_main')
    else:
        form = ProductForm()

    context = {'form': form}
    return render(request, "create_product.html", context)


def add_to_cart(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        cart = request.session.get('cart', [])

        # Convert UUID to string for storage in the session cart
        product_id_str = str(product_id)

        # Add product if it's not already in the cart
        if product_id_str not in cart:
            cart.append(product_id_str)

        # Update the session cart
        request.session['cart'] = cart
        
        return JsonResponse({'status': 'success', 'message': 'Product added to cart.'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})

def cart_view(request):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')  # Use .get to avoid KeyError
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)  # Get products in cart
    total_price = sum(product.price for product in products)  # Calculate total price
    return render(request, 'cart.html', {'products': products, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart = request.session.get('cart', [])

    # Ensure the product_id is a string before comparison
    product_id_str = str(product_id)

    if product_id_str in cart:
        cart.remove(product_id_str)  # Remove the product from the cart
        request.session['cart'] = cart  # Update the cart in the session

    return redirect('main:cart')  # Redirect back to the cart page



def checkout(request):
    if request.method == 'GET':
        # Assuming your cart is stored in the session
        cart = request.session.get('cart', [])
        user = request.user  # Get the currently logged-in user
        
        # Create Purchase records for each product in the cart
        for product_id in cart:
            product = Product.objects.get(id=product_id)  # Ensure to handle exceptions in production code
            Purchase.objects.create(user=user, product=product)

        # Clear the cart after checkout
        request.session['cart'] = []

        # Redirect to the library page
        return redirect('main:show_main')

def library(request):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')  # Use .get to avoid KeyError
    purchases = Purchase.objects.filter(user=request.user)
    return render(request, 'library.html', {'purchases': purchases})

def edit_review(request, purchase_id):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')  # Use .get to avoid KeyError
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('main:library')  # Redirect to the library page
    else:
        form = ReviewForm(instance=purchase)
    return render(request, 'edit_review.html', {'form': form, 'purchase': purchase})

def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    purchase.delete()
    return redirect('main:library')  # Redirect to the library page


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

def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
            user = form.get_user()
            login(request, user)
            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(datetime.datetime.now()))
            return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response
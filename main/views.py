from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProductForm, ReviewForm
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import datetime
from django.urls import reverse
from .models import Product, Purchase, Thread,Reply,Like
from django.views.decorators.http import require_POST
from django.utils.html import strip_tags
import bleach

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

        # Retrieve the cart from the session or create a new one if it doesn't exist
        cart = request.session.get('cart', [])

        product_id_str = str(product_id)  # Ensure product ID is stored as string

        if product_id_str not in cart:
            cart.append(product_id_str)  # Add product to cart

        # Update session cart
        request.session['cart'] = cart
        request.session.modified = True  # Ensure session gets saved

        # Return a success response
        return JsonResponse({'status': 'success', 'message': 'Product added to cart.'})
    
    # Return an error if request is invalid
    return JsonResponse({'status': 'error', 'message': 'Invalid request.'}, status=400)

def remove_from_cart(request, product_id):
    if request.method == 'POST':
        cart = request.session.get('cart', [])
        product_id_str = str(product_id)

        if product_id_str in cart:
            cart.remove(product_id_str)
            request.session['cart'] = cart
            
            # Recalculate total price and total items
            products = Product.objects.filter(id__in=cart)
            total_price = sum(product.price for product in products)
            total_items = len(products)

            return JsonResponse({
                'status': 'success', 
                'message': 'Product removed from cart.',
                'total_price': total_price,
                'total_items': total_items
            })

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})


def cart_view(request):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')
    cart = request.session.get('cart', [])
    products = Product.objects.filter(id__in=cart)
    total_price = sum(product.price for product in products)
    
    return render(request, 'cart.html', {'products': products, 'total_price': total_price})

def checkout(request):
    if request.method == 'GET':
        cart = request.session.get('cart', [])
        user = request.user
        
        for product_id in cart:
            product = Product.objects.get(id=product_id)
            Purchase.objects.create(user=user, product=product)

        request.session['cart'] = []

        return redirect('main:show_main')

def library(request):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')
    purchases = Purchase.objects.filter(user=request.user)
    
    return render(request, 'library.html', {'purchases': purchases})

def edit_review(request, purchase_id):
    user_name = request.user.username if request.user.is_authenticated else "Guest"
    last_login = request.COOKIES.get('last_login', 'Never')
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, instance=purchase)
        if form.is_valid():
            form.save()
            return redirect('main:library')
    else:
        form = ReviewForm(instance=purchase)
    
    return render(request, 'edit_review.html', {'form': form, 'purchase': purchase})

def delete_purchase(request, purchase_id):
    purchase = get_object_or_404(Purchase, id=purchase_id, user=request.user)
    purchase.delete()
    
    return redirect('main:library')

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
    
    context = {'form': form}
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


# Display the list of forums (based on products owned by the user)
@login_required
def community(request):
    # Fetch all purchases for the logged-in user
    purchases = Purchase.objects.filter(user=request.user)
    
    # Fetch the products associated with those purchases
    products = [purchase.product for purchase in purchases]

    context = {
        'products': products,
    }
    return render(request, 'community.html', context)



# Display threads in a specific forum
@login_required
def forum_threads(request, product_id):
    # Fetch the product based on the ID
    product = get_object_or_404(Product, id=product_id)
    
    # Fetch threads related to this product
    threads = Thread.objects.filter(product=product)

    context = {
        'product': product,
        'threads': threads
    }
    return render(request, 'forum.html', context)



# Display replies in a specific thread
@login_required
def thread_replies(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id)
    replies = Reply.objects.filter(thread=thread)
    return render(request, 'thread_replies.html', {'thread': thread, 'replies': replies})

# Create a new thread in a forum
@login_required
@require_POST
def create_thread(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        title = strip_tags(request.POST.get('title'))
        content = strip_tags(request.POST.get('content'))
        # Clean the input data
        clean_title = bleach.clean(title)
        clean_content = bleach.clean(content)

        if not clean_title or not clean_content:
            return JsonResponse({'status': 'error', 'message': 'Title and content cannot be empty.'})

        # Create the thread
        thread = Thread.objects.create(
            title=clean_title,
            content=clean_content,
            user=request.user,
            product=product
        )

        return JsonResponse({
            'status': 'success',
            'thread': {
                'id': thread.id,
                'title': thread.title,
                'content': thread.content,
                'user': request.user.username,
                'created_at': thread.created_at.strftime('%Y-%m-%d %H:%M:%S'),
            }
        })

    return JsonResponse({'status': 'error', 'message': 'Invalid request.'})
# Create a new reply in a thread
@login_required
@require_POST
def create_reply(request, thread_id):
    if request.method == 'POST':
        thread = get_object_or_404(Thread, id=thread_id)
        content = request.POST.get('content')

        # Create the reply
        new_reply = Reply.objects.create(
            thread=thread,
            user=request.user,
            content=content
        )
        return JsonResponse({'status': 'success', 'message': 'Reply created successfully!'})
    
    return JsonResponse({'status': 'error', 'message': 'Failed to create reply'})

# Like a reply
@login_required
@require_POST
def like_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id)

    # Check if the user has already liked this reply
    if not Like.objects.filter(user=request.user, reply=reply).exists():
        Like.objects.create(user=request.user, reply=reply)
        return JsonResponse({'status': 'success', 'message': 'Reply liked!'})
    
    return JsonResponse({'status': 'error', 'message': 'You have already liked this reply'})

# Delete a thread (only if the user is the owner)
@login_required
@require_POST
def delete_thread(request, thread_id):
    thread = get_object_or_404(Thread, id=thread_id, user=request.user)
    thread.delete()
    return JsonResponse({'status': 'success', 'message': 'Thread deleted successfully!'})

# Delete a reply (only if the user is the owner)
@login_required
@require_POST
def delete_reply(request, reply_id):
    reply = get_object_or_404(Reply, id=reply_id, user=request.user)
    reply.delete()
    return JsonResponse({'status': 'success', 'message': 'Reply deleted successfully!'})
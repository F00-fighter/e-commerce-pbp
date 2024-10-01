from django.urls import path
from main.views import show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id, register, login_user, logout_user,add_to_cart, cart_view, remove_from_cart, checkout, library, edit_review, delete_purchase
import uuid

app_name = 'main'

urlpatterns = [
    path('', show_main, name='show_main'),
    path('create-product', create_product, name='create_product'),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
    path('add_to_cart/<uuid:product_id>/', add_to_cart, name='add_to_cart'),
    path('shopping-cart/', cart_view, name='cart'),
    path('shopping-cart/remove/<uuid:product_id>/', remove_from_cart, name='remove_from_cart'),
    path('checkout/', checkout, name='checkout'),
    path('library/', library, name="library"),
    path('purchase/edit/<int:purchase_id>/', edit_review, name='edit_review'),
    path('purchase/delete/<int:purchase_id>/', delete_purchase, name='delete_purchase'),
]
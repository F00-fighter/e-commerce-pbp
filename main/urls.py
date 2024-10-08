from django.urls import path
from . import views
import uuid

app_name = 'main'

urlpatterns = [
    path('', views.show_main, name='show_main'),
    path('create-product', views.create_product, name='create_product'),
    path('xml/', views.show_xml, name='show_xml'),
    path('json/', views.show_json, name='show_json'),
    path('xml/<str:id>/', views.show_xml_by_id, name='show_xml_by_id'),
    path('json/<str:id>/', views.show_json_by_id, name='show_json_by_id'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('add_to_cart/<uuid:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('shopping-cart/', views.cart_view, name='cart'),
    path('remove_from_cart/<uuid:product_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('library/', views.library, name="library"),
    path('purchase/edit/<int:purchase_id>/', views.edit_review, name='edit_review'),
    path('purchase/delete/<int:purchase_id>/', views.delete_purchase, name='delete_purchase'),
    path('community/', views.community, name='community'),
    path('community/forum/<uuid:product_id>/', views.forum_threads, name='forum_threads'),
    path('community/thread/<uuid:thread_id>/', views.thread_replies, name='thread_replies'),
    path('community/forum/<uuid:product_id>/create-thread/', views.create_thread, name='create_thread'),
    path('community/thread/<uuid:thread_id>/create-reply/', views.create_reply, name='create_reply'),
    path('community/reply/<uuid:reply_id>/like/', views.like_reply, name='like_reply'),
    path('community/thread/<uuid:thread_id>/delete/', views.delete_thread, name='delete_thread'),
    path('community/reply/<uuid:reply_id>/delete/', views.delete_reply, name='delete_reply'),
]
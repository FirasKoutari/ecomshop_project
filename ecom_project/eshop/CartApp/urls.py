from django.urls import path
from . import views
# from .views import add_to_cart

# app_name = 'CartApp'\
# app_name = 'cart'

# urlpatterns = [
#     path('cart/', views.cart, name='cart'),
#     # path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
#     path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
#     path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
#     # ... other patterns ...
# ]

app_name = 'CartApp'

urlpatterns = [
    path('cart/', views.view_cart, name='view_cart'),
    path('add/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', views.remove_from_cart, name='remove_from_cart'),
    path('shop/', views.product_list, name='product_list'),
    path('add_to_wishlist/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('remove_from_wishlist/<int:wishlist_item_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),
    path('wishlist/', views.wishlist, name='wishlist'),
]
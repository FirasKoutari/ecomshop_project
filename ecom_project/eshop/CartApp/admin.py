from django.contrib import admin
from .models import ShoppingCart
from .models import Product, CartItem


admin.site.register(ShoppingCart)
admin.site.register(CartItem)

# admin.site.register(ShoppingCartItem)


# Register your models here.

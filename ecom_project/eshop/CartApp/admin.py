from django.contrib import admin
from .models import ShoppingCart
from .models import Product, CartItem,WishlistItem


admin.site.register(ShoppingCart)
admin.site.register(CartItem)
admin.site.register(WishlistItem)

# admin.site.register(ShoppingCartItem)


# Register your models here.

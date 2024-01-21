# CartApp/context_processors.py
from .models import CartItem
from django.db.models import Sum

def cart_total_quantity(request):
    total_quantity = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_quantity = cart_items.aggregate(Sum('quantity'))['quantity__sum'] or 0

    return {'total_quantity': total_quantity}

from .models import WishlistItem

def wishlist_count(request):
    if request.user.is_authenticated:
        return {'wishlist_count': WishlistItem.objects.filter(user=request.user).count()}
    return {'wishlist_count': 0}
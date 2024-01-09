# CartApp/context_processors.py
from .models import CartItem
from django.db.models import Sum

def cart_total_quantity(request):
    total_quantity = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return {'total_quantity': total_quantity}

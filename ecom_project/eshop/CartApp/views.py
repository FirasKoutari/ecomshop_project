from django.shortcuts import render
from django.db.models.signals import post_save
from django.db import models
from ProductsApp.models import Product
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum

# Create your views here.
def cart(request):
    return render(request,'cart.html')
# eshop/views.py


# def add_to_cart(request, product_item_id):
#     product_item = get_object_or_404(ProductItem, pk=product_item_id)
#     cart = Cart(request)
#     cart.add(product_item=product_item)
#     return redirect('cart')

# eshop/views.py
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from CartApp.models import CartItem


def view_cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})
 




def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.qty <= 0:
        messages.error(request, f"Sorry, {product.name} is out of stock.")
        return redirect(request.META.get('HTTP_REFERER', 'CartApp:view_cart'))

    cart_item, created = CartItem.objects.get_or_create(product=product, user=request.user)

    if not created:
        if cart_item.quantity < product.qty:
            cart_item.quantity += 1
            cart_item.save()
            product.qty -= 1  
            product.save()
            messages.success(request, f"Quantity of {product.name} increased to {cart_item.quantity}.")
            return redirect('CartApp:view_cart')

        else:
            messages.warning(request, f"Cannot add more {product.name} to the cart. Limited stock available.")
    else:
        cart_item.quantity = 1
        cart_item.save()
        product.qty -= 1  
        product.save()
        messages.success(request, f"{product.name} added to the cart.")

    return redirect(request.META.get('HTTP_REFERER', 'CartApp:view_cart'))




def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('CartApp:view_cart')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})

# Had lfonction dyali l'image li fl topbar

def cart_total_quantity(request):
    total_quantity = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
    return {'total_quantity': total_quantity}


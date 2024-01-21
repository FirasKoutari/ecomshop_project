from django.shortcuts import render
from django.db.models.signals import post_save
from django.db import models
from ProductsApp.models import Product
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.db.models import Sum
from django.contrib.auth.models import AnonymousUser
from django.http import JsonResponse



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
from CartApp.models import CartItem , WishlistItem


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

pass




def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('CartApp:view_cart')
pass

def product_list(request):
    products = Product.objects.all()
    return render(request, 'shop.html', {'products': products})
pass
# Had lfonction dyali l'image li fl topbar

# def cart_total_quantity(request):
#     total_quantity = CartItem.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0
#     return {'total_quantity': total_quantity}


# @login_required
# def wishlist(request):
#     wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_at')
#     return render(request, 'wishlist.html', {'wishlist_items': wishlist_items})

@login_required
def wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user).order_by('-added_at')
    # wishlist_count = wishlist_items.count()
    return render(request, 'wishlist.html', {'wishlist_items': wishlist_items })



@login_required
def add_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)

    # Check if the product is already in the wishlist
    if WishlistItem.objects.filter(user=request.user, product=product).exists():
        messages.warning(request, 'Product is already in your wishlist.')
    else:
        # Add the product to the wishlist
        WishlistItem.objects.create(
            user=request.user,
            product=product,
            quantity=1,
        )
        messages.success(request, 'Product added to your wishlist.')

    return redirect('shop') 



@login_required
def remove_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, pk=wishlist_item_id)
    wishlist_item.delete()

    return redirect('CartApp:wishlist')

# @login_required
# def add_to_cart_from_wishlist(request, wishlist_item_id):
#     wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id)

#     # Ajoutez le produit au panier avec la quantité de la wishlist
#     cart_item, created = CartItem.objects.get_or_create(product=wishlist_item.product, user=request.user)
#     if not created and (cart_item.quantity + wishlist_item.quantity) > wishlist_item.product.qty:
#         messages.warning(request, f"Cannot add more {wishlist_item.product.name} to the cart. Limited stock available.")
#     else:
#         cart_item.quantity += wishlist_item.quantity
#         cart_item.save()
#         wishlist_item.delete()
#         messages.success(request, f"{wishlist_item.product.name} added to the cart.")

#     return redirect('CartApp:view_cart')



from django.http import JsonResponse

@login_required
def add_to_cart_from_wishlist(request, wishlist_item_id):
    wishlist_item = get_object_or_404(WishlistItem, id=wishlist_item_id)
    quantity = int(request.GET.get('quantity', 1))

    # Ajoutez le produit au panier avec la quantité spécifiée
    cart_item, created = CartItem.objects.get_or_create(product=wishlist_item.product, user=request.user)
    if not created and (cart_item.quantity + quantity) > wishlist_item.product.qty:
        messages.warning(request, f"Cannot add more {wishlist_item.product.name} to the cart. Limited stock available.")
    else:
        cart_item.quantity += quantity
        cart_item.save()
        wishlist_item.delete()
        messages.success(request, f"{wishlist_item.product.name} added to the cart.")

    return JsonResponse({'status': 'success'})


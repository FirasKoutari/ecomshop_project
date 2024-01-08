from django.shortcuts import render
from django.db.models.signals import post_save
from django.db import models
from ProductsApp.models import Product
from django.shortcuts import redirect, get_object_or_404

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
    product = Product.objects.get(id=product_id)
    cart_item, created = CartItem.objects.get_or_create(product=product, 
                                                       user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('CartApp:view_cart') 
def remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('CartApp:view_cart')


def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# @login_required
# def add_to_cart(request, product_item_id):
#     product_item = get_object_or_404(ProductItem, pk=product_item_id)

#     # Get or create the user's shopping cart
#     shopping_cart, created = ShoppingCart.objects.get_or_create(user=request.user)

#     # Check if the product item is already in the cart
#     cart_item, created = ShoppingCartItem.objects.get_or_create(cart=shopping_cart, product_item=product_item)
    
#     # If the item is already in the cart, increase the quantity
#     if not created:
#         cart_item.qty += 1
#         cart_item.save()

#     return redirect('cart')

# class ProductItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     product_id = models.IntegerField()  # Champ pour stocker directement l'ID du produit associé
#     sku = models.CharField(max_length=255)
#     qty_in_stock = models.IntegerField()
#     product_image = models.ImageField(upload_to='product_images/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)

#     def save(self, *args, **kwargs):
#         # Avant de sauvegarder, assurez-vous que product_id est l'ID du produit associé
#         if self.product:
#             self.product_id = self.product.id
#         super().save(*args, **kwargs)

#     def __str__(self):
#         return f"{self.product.name} - {self.sku}"
    


# def add_to_cart(request, product_id):
#     product_item = get_object_or_404(ProductItem, product_id=product_id)
#     cart = Cart(request)
#     cart.add(product_item=product_item)
#     return redirect('shop')  # Redirige où vous le souhaitez après l'ajout au panier
# # models.py



from ProductsApp.models import ProductConfiguration,ProductItem,ProductCategory,Variation,VariationOption,Product,Promotion,PromotionCategory
from django.shortcuts import render, get_object_or_404,redirect
from django.views import View
from .models import Product
from CartApp.models import ShoppingCart, ShoppingCartItem
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.http import HttpResponse
from django.contrib import messages
from CartApp.models import ShoppingCart
from django.db.models import Exists, OuterRef
from django.db.models import Subquery


# Create your views here.
def detail(request):
    return render(request,'detail.html')





def shop(request):
    prod = Product.objects.all()
    return render(request,'shop.html', {'prod': prod})



class ProductDetailView(View):
    template_name = 'detail.html'
    model = Product
    context_object_name = 'product'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        context = {'product': product}
        return render(request, self.template_name, context)
    





# @method_decorator(login_required, name='dispatch')
# class AddToCartView(View):
#     # ... (autres parties de la classe)

#     def get(self, request, pk):
#         # Vérifier si l'utilisateur est connecté
#         if not request.user.is_authenticated:
#             return redirect('login')  # Rediriger vers la page de connexion si l'utilisateur n'est pas connecté

#         product = get_object_or_404(Product, pk=pk)

#         # Vérifier si l'utilisateur a un panier existant, sinon le créer
#         print(type(request.user))
#         cart, created = ShoppingCart.objects.get_or_create(user=request.user)
#         print(f"Cart ID: {cart.id}, User: {cart.user}")

#         # Vérifier si le produit est déjà dans le panier, sinon le créer
#         cart_item, item_created = ShoppingCartItem.objects.get_or_create(cart=cart, product_item=product)

#         # Si le produit est déjà dans le panier, augmenter la quantité
#         if not item_created:
#             cart_item.qty += 1
#             cart_item.save()

#         return redirect('cart')  # Rediriger vers la page du panier


# def add_to_cart_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     # Check if the user is logged in
#     if not request.user.is_authenticated:
#         # Redirect to the login page or handle it accordingly
#         messages.error(request, 'Please log in to add items to your cart.')
#         return HttpResponse(status=401)

#     # Get or create the user's shopping cart
#     cart, created = ShoppingCart.objects.get_or_create(user=request.user)

#     # Add the product to the cart
#     cart.products.add(product)
#     cart.save()

#     # Display a success message
#     messages.success(request, f'{product.name} added to your cart successfully!')

#     # You can redirect to a specific page or just return a response
#     return HttpResponse(status=200)

# def add_to_cart_view(request, pk):
#     product = get_object_or_404(Product, pk=pk)

#     # Check if the user is logged in
#     if not request.user.is_authenticated:
#         # Redirect to the login page or handle it accordingly
#         messages.error(request, 'Please log in to add items to your cart.')
#         return HttpResponse(status=401)

#     # Get or create the user's shopping cart
#     cart, _ = ShoppingCart.objects.get_or_create(user=request.user)

#     # Add the product to the cart
#     cart.products.add(product)
#     cart.save()

#     # Display a success message
#     messages.success(request, f'{product.name} added to your cart successfully!')

#     # You can redirect to a specific page or just return a response
#     return HttpResponse(status=200)



# def add_to_cart_view(request, pk):
#     product_item = get_object_or_404(ProductItem, pk=pk)

#     # Check if the user is logged in
#     if not request.user.is_authenticated:
#         # Redirect to the login page or handle it accordingly
#         messages.error(request, 'Please log in to add items to your cart.')
#         return HttpResponse(status=401)

#     # Get or create the user's shopping cart
#     cart, _ = ShoppingCart.objects.get_or_create(user=request.user)

#     # Add the product to the cart
#     cart_item, created = cart.shoppingcartitem_set.get_or_create(product_item=product_item)
#     if not created:
#         # If the item already exists in the cart, you may want to increment the quantity
#         cart_item.qty += 1
#         cart_item.save()

#     # Display a success message
#     messages.success(request, f'{product_item.name} added to your cart successfully!')

#     # You can redirect to a specific page or just return a response
#     return HttpResponse(status=200)






def add_to_cart_view(request, pk):
    try:
        product_item = get_object_or_404(ProductItem, pk=pk)
    except ProductItem.DoesNotExist:
        messages.error(request, 'Product not found')
        return HttpResponse(status=404)

    # Debugging: Print the product item's name and ID
    print(f"ProductItem ID: {pk}, Name: {product_item.name}")

    # Check if the user is logged in
    if not request.user.is_authenticated:
        # Redirect to the login page or handle it accordingly
        messages.error(request, 'Please log in to add items to your cart.')
        return HttpResponse(status=401)

    # Get or create the user's shopping cart
    cart, _ = ShoppingCart.objects.get_or_create(user=request.user)

    # Add the product to the cart
    cart_item, created = cart.shoppingcartitem_set.get_or_create(product_item=product_item)
    if not created:
        # If the item already exists in the cart, you may want to increment the quantity
        cart_item.qty += 1
        cart_item.save()

    # Display a success message
    messages.success(request, f'{product_item.name} added to your cart successfully!')

    # You can redirect to a specific page or just return a response
    return HttpResponse(status=200)



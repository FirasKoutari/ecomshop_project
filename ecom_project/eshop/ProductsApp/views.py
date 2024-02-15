import operator
from AuthenticationApp import models
from django.db.models import Q
from functools import reduce
from operator import or_
from ProductsApp.models import Product,ProductCategory
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product ,Review
from CartApp.models import ShoppingCart
from django.http import HttpResponse
from django.contrib import messages
from CartApp.models import ShoppingCart
from .models import Product
from .forms import ReviewForm


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
        reviews = Review.objects.filter(product=product)  # Récupérez les commentaires associés au produit
        context = {'product': product, 'reviews': reviews}  # Ajoutez les commentaires au contexte
        return render(request, self.template_name, context)


# class ProductDetailView(View):
#     template_name = 'detail.html'
#     model = Product
#     context_object_name = 'product'

#     def get(self, request, pk):
#      product = get_object_or_404(Product, pk=pk)
#      reviews = product.reviews.all()
#      print(reviews)  # Ajoutez cette ligne pour imprimer les commentaires dans la console
#      context = {'product': product, 'reviews': reviews}
#      return render(request, self.template_name, context)
    

# class ProductDetailView(View):
#     template_name = 'detail.html'
#     model = Product
#     context_object_name = 'product'

#     def get(self, request, pk):
#         product = get_object_or_404(Product, pk=pk)
#         context = {'product': product}
#         return render(request, self.template_name, context)
    
    # views.py
# views.py
# ProductsApp/views.py
# views.py
# views.py



def add_review(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.product = product
            new_review.user = request.user
            new_review.save()
            return redirect('detail', pk=product_id)  # Changez product_id à pk
    else:
        form = ReviewForm()

    return render(request, 'add_review.html', {'form': form, 'product': product})


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




def category_product_list_view(request, cid):
    category = get_object_or_404(ProductCategory, id=cid)
    products = Product.objects.filter(category=category)

    # Filter by price
    price_filter = request.GET.getlist('price-all')
    if price_filter:
        # If "All Price" is selected, no need to filter by price
        pass
    else:
        price_ranges = ['price-1', 'price-2', 'price-3', 'price-4', 'price-5']
        selected_ranges = [range_key for range_key in price_ranges if request.GET.get(range_key)]
        if selected_ranges:
            # Filter products based on selected price ranges
            price_filters = {
                'price-1': (0, 100),
                'price-2': (100, 200),
                'price-3': (200, 300),
                'price-4': (300, 400),
                'price-5': (400, 500),
            }
            price_query = reduce(operator.or_, [Q(price__range=price_filters[key]) for key in selected_ranges])
            products = products.filter(price_query)


    context = {
        "category": category,
        "products": products,
    }
    return render(request, "category.html", context)




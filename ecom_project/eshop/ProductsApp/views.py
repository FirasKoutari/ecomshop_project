import operator
from AuthenticationApp import models
from django.db.models import Q
from functools import reduce
from operator import or_
from ProductsApp.models import Product,ProductCategory
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .models import Product ,Review
from ProductsApp.models import ProductItem
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






def index(request):
    prod = Product.objects.all()
    return render(request, 'index.html', {'prod': prod})

def contact(request):
    return render(request, 'contact.html')


def shop1(request):
    query = request.GET.get('q')
    if query:
        print(f"Query: {query}")  # Debugging line
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    print(f"Products: {products}")  # Debugging line
    return render(request, 'shop1.html', {'prod': products})



def products_view(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(name__icontains=query)
    else:
        products = Product.objects.all()
    
    # Ajoutez une impression pour le débogage
    print(f"Query: {query}, Products: {products}")
    
    return render(request, 'shop_products.html', {'products': products})




from django.shortcuts import render, redirect
from .models import Product  # Update path if using a different app




from .forms import PriceRangeForm

def shop_filter(request):
    products = Product.objects.all()  # Initial queryset

    # Handle price filtering based on request parameters:
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if min_price and max_price:
        try:
            min_price = float(min_price)
            max_price = float(max_price)
            products = products.filter(price__gte=min_price, price__lte=max_price)
        except ValueError:
            pass  # Handle invalid price values gracefully (optional)

    # Handle sorting based on request parameters (optional):
    sort_by = request.GET.get('sort_by')
    if sort_by:
        if sort_by == 'price_asc':
            products = products.order_by('price')
        elif sort_by == 'price_desc':
            products = products.order_by('-price')

    # Create an instance of the PriceRangeForm
    form = PriceRangeForm(initial={'min_price': min_price, 'max_price': max_price})

    context = {
        'products': products,
        'form': form,
        # Add other context variables as needed
    }

    return render(request, 'shop_filter.html', context)

from .models import Orders
from . import forms 

def my_order_view(request):
    user = request.user
    orders = Orders.objects.filter(user=user)
    ordered_products = [order.product for order in orders]

    return render(request, 'my_order.html', {'data': zip(ordered_products, orders)})



# def update_order_view(request, pk):
#     order = Orders.objects.get(id=pk)
#     orderForm = forms.OrderForm(instance=order)
#     if request.method == 'POST':
#         orderForm = forms.OrderForm(request.POST, instance=order)
#         if orderForm.is_valid():
#             orderForm.save()
#             return redirect('admin-view-booking')
#     return render(request, 'update_order.html', {'orderForm': orderForm})


def delete_order_view(request, pk):
    order = Orders.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')


def admin_view_booking_view(request):
    orders = Orders.objects.all()
    ordered_products = [order.product for order in orders]
    ordered_bys = [order.user for order in orders]

    return render(request, 'admin_view_booking.html', {'data': zip(ordered_products, ordered_bys, orders)})


import io
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    html  = template.render(context_dict)
    result = io.BytesIO()
    pdf = pisa.pisaDocument(io.BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return


def download_invoice_view(request,orderID,productID):
    order=models.Orders.objects.get(id=orderID)
    product=models.Product.objects.get(id=productID)
    mydict={
        'orderDate':order.order_date,
        'customerName':request.user,
        'customerEmail':order.email,
        'customerMobile':order.mobile,
        'shipmentAddress':order.address,
        'orderStatus':order.status,

        'productName':product.name,
        'productImage':product.product_image,
        'productPrice':product.price,
        'productDescription':product.description,


    }
    return render_to_pdf('download_invoice.html',mydict)


from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Orders

@login_required
def my_order_view(request):
    user = request.user
    orders = Orders.objects.filter(user=user)
    ordered_products = [order.product for order in orders]
    return render(request, 'my_order.html', {'data': zip(ordered_products, orders)})


from django.shortcuts import render, redirect, get_object_or_404
from .forms import OrderForm
from .models import Orders



def update_order_view(request, pk):
    order = get_object_or_404(Orders, id=pk)
    orderForm = OrderForm(instance=order)
    
    if request.method == 'POST':
        orderForm = OrderForm(request.POST, instance=order)
        if orderForm.is_valid():
            orderForm.save()
            print("Order status updated successfully!")  # Debug statement
            return redirect('admin-view-booking')
        else:
            print("Form is not valid")  # Debug statement
            print(orderForm.errors)  # Print form errors for debugging
    
    return render(request, 'update_order.html', {'orderForm': orderForm})







from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from CartApp.models import ShoppingCart,CartItem 
from .models import Order, OrderItem 
from ProductsApp.models import Product
from PaymentApp.models import CreditCard






@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        shipping_cost = 10  # You can calculate shipping cost based on your logic
        total_price += shipping_cost
        

        billing_email = request.POST.get('billing_email')
        billing_mobile_no = request.POST.get('billing_mobile_no')
        billing_address_line1 = request.POST.get('billing_address_line1')



        shipping_email = request.POST.get('shipping_email')
        shipping_mobile_no = request.POST.get('shipping_mobile_no')
        shipping_address_line1 = request.POST.get('shipping_address_line1')

        payment_method = request.POST.get('payment')
        # Create an order
        order = Order.objects.create(

            user=request.user,

            billing_email=billing_email,
            billing_mobile_no=billing_mobile_no,
            billing_address_line1=billing_address_line1,



            shipping_email=shipping_email,
            shipping_mobile_no=shipping_mobile_no,
            shipping_address_line1=shipping_address_line1,


            payment_method=payment_method,
            total_price=total_price
        )
        # Create order items and update order total price
        for cart_item in cart_items:
            OrderItem.objects.create(order=order, cart_item=cart_item)
        # Save the final total price to the order
        order.save()
        # Clear the user's shopping cart
        cart_items.delete()
        
        
        return redirect('add_card')  
    
    # If the request method is not POST, retrieve cart items and calculate prices
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_cost = 10  # You can calculate shipping cost based on your logic
    total_price += shipping_cost
    return render(request, 'checkout.html', {'cart_items': cart_items, 'total_price': total_price, 'subtotal': subtotal, 'shipping_cost': shipping_cost})



def order_success(request):
    return render(request, 'card.html')

@login_required
def add_card(request):
    if request.method == 'POST':
        card_name = request.POST.get('card_name')
        card_number = request.POST.get('card_number')
        exp_month = request.POST.get('exp_month')
        exp_year = request.POST.get('exp_year')
        cvv = request.POST.get('cvv')

        # Create and save the credit card information
        CreditCard.objects.create(
            user=request.user,
            card_name=card_name,
            card_number=card_number,
            exp_month=exp_month,
            exp_year=exp_year,
            cvv=cvv
        )

        messages.success(request, 'Card added successfully!')
        return redirect('checkout')

    return render(request, 'add_card.html')

# # views.py

# from django.shortcuts import render, redirect
# from django.contrib import messages
# from .models import Order

# def add_card(request):
#     if request.method == 'POST':
#         card_name = request.POST.get('card_name')
#         card_number = request.POST.get('card_number')
#         exp_month = request.POST.get('exp_month')
#         exp_year = request.POST.get('exp_year')
#         cvv = request.POST.get('cvv')

#         # Simulate saving card information (you should handle this securely in production)
#         # Here we assume the card is added successfully and create an order
#         product_id = request.session.get('product_id')  # Retrieve product ID from session or wherever you store it

#         if product_id:
#             product = Product.objects.get(pk=product_id)
#             order = Order.objects.create(
#                 product=product,
#                 address='123 Sample Address, City, Country',  # Example address, you should get this from the user
#                 status='Pending'  # Initial status
#             )
#             order.save()

#             messages.success(request, 'Card added and order created successfully!')
#             return redirect('order_page')  # Redirect to order page after successful submission
#         else:
#             messages.error(request, 'Failed to add card. Product ID not found.')
#             return redirect('add_card')  # Redirect back to add card page if product ID is missing

#     return render(request, 'add_card.html')

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import CartItem, OrderItem
from django.contrib.auth.models import User
from ProductsApp.models import Orders


@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        shipping_cost = 10  # You can calculate shipping cost based on your logic
        total_price += shipping_cost

        billing_email = request.POST.get('billing_email')
        billing_mobile_no = request.POST.get('billing_mobile_no')
        billing_address_line1 = request.POST.get('billing_address_line1')

        shipping_email = request.POST.get('shipping_email')
        shipping_mobile_no = request.POST.get('shipping_mobile_no')
        shipping_address_line1 = request.POST.get('shipping_address_line1')

        payment_method = request.POST.get('payment')

        # Create orders for each cart item
        for cart_item in cart_items:
            Orders.objects.create(
                user=request.user,
                product=cart_item.product,
                email=billing_email,
                mobile=billing_mobile_no,
                address=billing_address_line1,
                status='Pending'
            )

        # Clear the user's shopping cart
        cart_items.delete()
        
        return redirect('add_card')
    
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    subtotal = sum(item.product.price * item.quantity for item in cart_items)
    shipping_cost = 10  # You can calculate shipping cost based on your logic
    total_price += shipping_cost
    
    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total_price': total_price,
        'subtotal': subtotal,
        'shipping_cost': shipping_cost
    })

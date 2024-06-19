
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
from CartApp.models import ShoppingCart,CartItem
from .models import Order, OrderItem ,CreditCard



@login_required
def checkout(request):
    if request.method == 'POST':
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.product.price * item.quantity for item in cart_items)
        subtotal = sum(item.product.price * item.quantity for item in cart_items)
        shipping_cost = 10  # You can calculate shipping cost based on your logic
        total_price += shipping_cost
        
        billing_first_name = request.POST.get('billing_first_name')
        billing_last_name = request.POST.get('billing_last_name')
        billing_email = request.POST.get('billing_email')
        billing_mobile_no = request.POST.get('billing_mobile_no')
        billing_address_line1 = request.POST.get('billing_address_line1')
        billing_address_line2 = request.POST.get('billing_address_line2')
        billing_country = request.POST.get('billing_country')
        billing_city = request.POST.get('billing_city')
        billing_state = request.POST.get('billing_state')
        billing_zip_code = request.POST.get('billing_zip_code')

        shipping_first_name = request.POST.get('shipping_first_name')
        shipping_last_name = request.POST.get('shipping_last_name')
        shipping_email = request.POST.get('shipping_email')
        shipping_mobile_no = request.POST.get('shipping_mobile_no')
        shipping_address_line1 = request.POST.get('shipping_address_line1')
        shipping_address_line2 = request.POST.get('shipping_address_line2')
        shipping_country = request.POST.get('shipping_country')
        shipping_city = request.POST.get('shipping_city')
        shipping_state = request.POST.get('shipping_state')
        shipping_zip_code = request.POST.get('shipping_zip_code')
        payment_method = request.POST.get('payment')
        # Create an order
        order = Order.objects.create(

            user=request.user,
            billing_first_name=billing_first_name,
            billing_last_name=billing_last_name,
            billing_email=billing_email,
            billing_mobile_no=billing_mobile_no,
            billing_address_line1=billing_address_line1,
            billing_address_line2=billing_address_line2,
            billing_country=billing_country,
            billing_city=billing_city,
            billing_state=billing_state,
            billing_zip_code=billing_zip_code,

            shipping_first_name=shipping_first_name,
            shipping_last_name=shipping_last_name,
            shipping_email=shipping_email,
            shipping_mobile_no=shipping_mobile_no,
            shipping_address_line1=shipping_address_line1,
            shipping_address_line2=shipping_address_line2,
            shipping_country=shipping_country,
            shipping_city=shipping_city,
            shipping_state=shipping_state,
            shipping_zip_code=shipping_zip_code,

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
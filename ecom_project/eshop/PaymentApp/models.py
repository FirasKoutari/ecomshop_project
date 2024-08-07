from django.db import models
from django.contrib.auth.models import User


from CartApp.models import CartItem


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    billing_email = models.EmailField()
    billing_mobile_no = models.CharField(max_length=15)
    billing_address_line1 = models.CharField(max_length=255)
    shipping_email = models.EmailField()
    shipping_mobile_no = models.CharField(max_length=15)
    shipping_address_line1 = models.CharField(max_length=255)
    payment_method = models.CharField(max_length=50)
    
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order #{self.pk} - {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.cart_item.quantity} x {self.cart_item.product.name} - ${self.cart_item.total_price}"
    





# # PaymentApp/models.py

# # PaymentApp/models.py

# from django.db import models
# from CartApp.models import CartItem
# from ProductsApp.models import ProductCategory  # Importez les modèles nécessaires de ProductsApp

# class OrderItem(models.Model):
#     order = models.ForeignKey('Order', on_delete=models.CASCADE)
#     cart_item = models.ForeignKey(CartItem, on_delete=models.CASCADE)
#     product = models.ForeignKey('ProductsApp.Product', on_delete=models.CASCADE)  # Utilisation de la chaîne de caractères pour éviter la circularité

#     def __str__(self):
#         return f"{self.cart_item.quantity} x {self.product.name} - ${self.cart_item.total_price}"

# class Order(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     billing_email = models.EmailField()
#     billing_mobile_no = models.CharField(max_length=15)
#     billing_address_line1 = models.CharField(max_length=255)
#     shipping_email = models.EmailField()
#     shipping_mobile_no = models.CharField(max_length=15)
#     shipping_address_line1 = models.CharField(max_length=255)
#     payment_method = models.CharField(max_length=50)
    
#     order_date = models.DateTimeField(auto_now_add=True)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)

#     def __str__(self):
#         return f"Order #{self.pk} - {self.user.username}"



class CreditCard(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    card_name = models.CharField(max_length=255)
    card_number = models.CharField(max_length=19)
    exp_month = models.CharField(max_length=2)
    exp_year = models.CharField(max_length=4)
    cvv = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.card_name} - {self.card_number[-4:]}"
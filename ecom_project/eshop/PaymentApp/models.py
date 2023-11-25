from django.db import models
from AuthenticationApp.models import User
from ProductsApp.models import ProductItem

# Create your models here.

class PaymentType(models.Model):
    value = models.CharField(max_length=255)

class UserPaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    provider = models.CharField(max_length=255)
    account_number = models.CharField(max_length=255)
    expiry_date = models.DateField()
    is_default = models.BooleanField()

class ShopOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField()
    payment_method = models.ForeignKey(UserPaymentMethod, on_delete=models.CASCADE)
    shipping_address = models.ForeignKey('Address', on_delete=models.CASCADE)
    shipping_method = models.ForeignKey('ShippingMethod', on_delete=models.CASCADE)
    order_total = models.DecimalField(max_digits=10, decimal_places=2)
    order_status = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)

class OrderLine(models.Model):
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    order = models.ForeignKey('ShopOrder', on_delete=models.CASCADE)
    qty = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

class ShippingMethod(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)

class OrderStatus(models.Model):
    status = models.CharField(max_length=255)

class UserAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.ForeignKey('Address', on_delete=models.CASCADE)
    is_default = models.BooleanField()

class Address(models.Model):
    unit_number = models.CharField(max_length=255)
    street_number = models.CharField(max_length=255)
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    city = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    country = models.ForeignKey('Country', on_delete=models.CASCADE)

class Country(models.Model):
    country_name = models.CharField(max_length=255)
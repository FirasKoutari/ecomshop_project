from django.db import models
from AuthenticationApp.models import User
from ProductsApp.models import ProductItem
# Create your models here.
class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class ShoppingCartItem(models.Model):
    cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
    product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    qty = models.IntegerField()
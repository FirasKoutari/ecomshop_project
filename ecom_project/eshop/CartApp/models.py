# from django.db import models
# from AuthenticationApp.models import User
# from ProductsApp.models import ProductItem
# # Create your models here.
# # class ShoppingCart(models.Model):
# #     user = models.ForeignKey(User, on_delete=models.CASCADE)

# class ShoppingCart(models.Model):
#  user = models.OneToOneField(User, on_delete=models.CASCADE)



# class ShoppingCartItem(models.Model):
#     cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
#     product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
#     qty = models.IntegerField()

from django.db import models
from django.contrib.auth.models import User 
from ProductsApp.models import Product
from django.contrib.auth import get_user_model


class ShoppingCart(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.quantity} x {self.product.name}'

# class ProductItem(BaseProductItem):
#     cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
#     qty_in_cart = models.IntegerField(default=0)

#     def __str__(self):
#         return self.product.name


# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     quantity = models.PositiveIntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)
 
#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'
# class ShoppingCartItem(models.Model):
#     cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
#     product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
#     qty = models.IntegerField()


# CartApp.models.py
# CartApp.models.py

# class CartItem(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='cart_items')
#     quantity = models.PositiveIntegerField(default=0)
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     date_added = models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return f'{self.quantity} x {self.product.name}'

# class ShoppingCartItem(models.Model):
#     cart = models.ForeignKey(ShoppingCart, on_delete=models.CASCADE)
#     product_item_cart = models.ForeignKey(ProductItem, on_delete=models.CASCADE, related_name='shopping_cart_items_cart')
#     qty = models.IntegerField()







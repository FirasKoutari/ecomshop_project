from django.db import models
from ProductsApp.models import ProductItem
# Create your models here.

class User(models.Model):
    email_address = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255)

class UserReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ordered_product = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
    rating_value = models.IntegerField()
    comment = models.TextField()




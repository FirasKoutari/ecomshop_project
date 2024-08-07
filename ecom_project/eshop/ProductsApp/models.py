from django.db import models
from django.contrib.auth.models import User

class ProductCategory(models.Model):
    
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    category_name = models.CharField(max_length=255)
    def __str__(self):
        return self.category_name

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

class Variation(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


    

    from django.db import models

# class Product(models.Model):
#     name = models.CharField(max_length=100)
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     description = models.TextField(null=True)
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     qty = models.IntegerField()  # Make sure this line is present
#     image = models.ImageField(upload_to='products/')

#     def __str__(self):
#         return self.name
    

class VariationOption(models.Model):
    variation = models.ForeignKey(Variation, on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

    
class PromotionCategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)


# class Product(models.Model):
#     category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     product_image = models.ImageField(upload_to='product_images/')
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     qty_in_stock = models.IntegerField()
    
#     def __str__(self):
#         return self.name
    
class Review(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.product.name} - {self.created_at}"

class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty = models.IntegerField()
    image = models.ImageField(upload_to='products/')
    color = models.CharField(max_length=50, null=True)
    size = models.CharField(max_length=10, null=True)
    # reviews = models.ManyToManyField(Review, related_name='products')

    def __str__(self):
        return self.name
    


    
# class Product(models.Model):
# 	name = models.CharField(max_length=100)
# 	description = models.TextField(null=True)
# 	price = models.DecimalField(max_digits=10, decimal_places=2)
     
     
# 	image = models.ImageField(upload_to='products/')


# 	def __str__(self):
# 		return self.name





class ProductItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    sku = models.CharField(max_length=255)
    qty_in_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

# class ProductConfiguration(models.Model):
#     product_item = models.ForeignKey(ProductItem, on_delete=models.CASCADE)
#     variation_option = models.ForeignKey(VariationOption, on_delete=models.CASCADE)



class Orders(models.Model):
    STATUS =(
        ('Pending','Pending'),
        ('Order Confirmed','Order Confirmed'),
        ('Out for Delivery','Out for Delivery'),
        ('Delivered','Delivered'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product=models.ForeignKey('Product',on_delete=models.CASCADE,null=True)
    email = models.CharField(max_length=50,null=True)
    address = models.CharField(max_length=500,null=True)
    mobile = models.CharField(max_length=20,null=True)
    order_date= models.DateField(auto_now_add=True,null=True)
    status=models.CharField(max_length=50,null=True,choices=STATUS)



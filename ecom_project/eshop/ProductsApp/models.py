from django.db import models

# Create your models here.
class ProductConfiguration(models.Model):
    product_item = models.ForeignKey('ProductItem', on_delete=models.CASCADE)
    variation_option = models.ForeignKey('VariationOption', on_delete=models.CASCADE)

class ProductItem(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    sku = models.CharField(max_length=255)
    qty_in_stock = models.IntegerField()
    product_image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)

class VariationOption(models.Model):
    variation = models.ForeignKey('Variation', on_delete=models.CASCADE)
    value = models.CharField(max_length=255)

class Product(models.Model):
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    product_image = models.ImageField(upload_to='product_images/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    qty_in_stock = models.IntegerField()


class Variation(models.Model):
    category = models.ForeignKey('ProductCategory', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)

class ProductCategory(models.Model):
    parent_category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    category_name = models.CharField(max_length=255)

class PromotionCategory(models.Model):
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)
    promotion = models.ForeignKey('Promotion', on_delete=models.CASCADE)

class Promotion(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    start_date = models.DateField()
    end_date = models.DateField()

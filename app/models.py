from django.db import models
from django.contrib.auth.models import User
from django.utils.html import format_html
from datetime import datetime
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100,verbose_name="Category",help_text="Enter category name")
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Category-Images",help_text="Upload category image",verbose_name="Category image")
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name
    @property
    def Last_Updated(self):
        time = self.updated
        times=time.strftime("%m/%d/%Y, %H:%M:%S")
        return times
    @property
    def Category_Image(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
    class Meta:
        db_table = 'Categories'
        verbose_name = "Category "
        verbose_name_plural = "Categories "
    @property
    def Products_Count(self):
        items = self.products.all()
        return len(items)
class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="Category",help_text="Choose category",related_name="products")
    name = models.CharField(max_length=100,help_text="Enter product name",verbose_name="Product name")
    image = models.ImageField(upload_to="Product-Images",help_text="Upload product image",verbose_name="Product image")
    about = models.CharField(max_length=500,null=True,blank=True,verbose_name="Product Description",help_text="Enter product description")
    price = models.IntegerField(verbose_name="Product price",help_text="Enter category price")
    discount = models.IntegerField(verbose_name="Product discount price",help_text="Enter product discount price",default=0)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    @property
    def Last_Updated(self):
        time = self.updated
        times=time.strftime("%m/%d/%Y, %H:%M:%S")
        return times
    @property
    def Product_Image(self):
        return format_html('<img src="{}" width="50" height="50" style="border-radius:50%" />'.format(self.image.url))
    @property
    def user(self):
        return self.category.user
    def __str__(self):
        return self.name
    class Meta:
        db_table = 'Products'
        verbose_name = "Product "
        verbose_name_plural = "Products "
    
    
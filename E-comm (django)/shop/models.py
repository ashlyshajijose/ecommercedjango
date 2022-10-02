from contextlib import nullcontext
from distutils.command.upload import upload
from pyexpat import model
from tkinter import CASCADE
from tkinter.tix import Select
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):       #admin....
    product_category = models.CharField(max_length=100)

class Product(models.Model):        #admin....
    catgr = models.ForeignKey(Category,on_delete=models.CASCADE,null=True)
    Product_name = models.CharField(max_length=300)
    Product_detail = models.CharField(max_length=600)
    Product_price = models.IntegerField()
    Product_stock = models.IntegerField()
    Product_img = models.ImageField(upload_to='P_img', null=False)

class Cart(models.Model):       #user....
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    product_qty = models.IntegerField(null=True)

class Customer(models.Model):       #user....
    product =models.ForeignKey(Product,on_delete=models.CASCADE,null=True)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE,null=True)
    c_user=models.ForeignKey(User,on_delete=models.CASCADE,null=True)
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    Phone_numbr = models.BigIntegerField(10)
    E_mail = models.EmailField()
    Address = models.CharField(max_length=500)
    Pincode = models.IntegerField(6,null=True)
    Landmark = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='user_img',null=True)
from django.db import models
import datetime
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser
#category
#customer
#product
#order

# Create your models here.

    
class Category(models.Model):
    name = models.CharField(max_length=50)
    #menue = models.ForeignKey(Cmenue,on_delete=models.CASCADE,default=1)
 
    def __str__(self):
        return self.name 
    
class Cmenue(models.Model):
    name = models.CharField(max_length=50)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    vak = models.CharField(max_length=50)
    def __str__(self):
        return self.name 
    

class Customer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    first_name = models.CharField(max_length=50)
    last_name =  models.CharField(max_length=50)
    phone =  models.CharField(max_length=50)
    email =  models.EmailField(max_length=50)
    password = models.CharField(max_length=250,blank=True,null=True)
    old_c =  models.CharField(max_length=250,blank=True,null=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    Category = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    Category_M = models.ForeignKey(Cmenue,on_delete=models.CASCADE,default=1)
    description = models.CharField(max_length=250,default='',blank=True,null=True)
    image = models.ImageField(upload_to='uploads/product/',blank=True,null=True,default='')
    image2 = models.ImageField(upload_to='uploads/product/',blank=True,null=True,default='')
    is_sale = models.BooleanField(default=False)
    sale_price = models.DecimalField(default=0,decimal_places=2,max_digits=6)
    outsidelink = models.CharField(max_length=255,blank=True,null=True,default='')
    def __str__(self):
        return self.name
    #TODO prevent error if no img 
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
 
class Order(models.Model):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE,null=True,blank=True)
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    address = models.CharField(max_length=100,default='',blank=True)
    phone =   models.CharField(max_length=30,default='',blank=True)
    date = models.DateField(default=datetime.datetime.today)
    date_orderd = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False,blank=False,null=True)   
    transaction_id = models.CharField(max_length=200,null=True)
    def __str__(self):
        return str(self.id)
    
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
    
    
class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=1,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    
    
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total
    
    
class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    zipcode = models.CharField(max_length=200,null=True)
    date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    phone =   models.CharField(max_length=30,default='',blank=True)

    def __str__(self):
        # return self.address
        return str(self.order)

    
    
    

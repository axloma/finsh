from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Category,Customer,Product,Order,OrderItem,ShippingAddress,Cmenue

# Register your models here.

class AdminReg(admin.ModelAdmin):
    list_display = ('name','price','id')

class AccountInLine(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "Accounts"
    

class Customize_user_admin(UserAdmin):
    inlines = (AccountInLine,)
    #list_display("username")
    
admin.site.unregister(User)
admin.site.register(User,Customize_user_admin)
admin.site.register(Category)
admin.site.register(Cmenue)

admin.site.register(Customer)
admin.site.register(Product,AdminReg)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)




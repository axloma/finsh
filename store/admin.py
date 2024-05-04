from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from .models import Category,Customer,Product,Order,OrderItem,ShippingAddress,Cmenue

# Register your models here.

class AdminReg(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ('name','price','id','Category_M')

class AdminRe(admin.ModelAdmin):
    search_fields = ['order__id']
    list_display = [field.name for field in OrderItem._meta.get_fields()]

class AdminReO(admin.ModelAdmin):
    # search_fields = ['id']
    list_display = [field.name for field in Order._meta.get_fields()]
    # list_display = OrderItem._meta.get_all_field_names() 
    # list_display = ('order','id','product','quantity','date_added','product_id')
    # list_display = [__all__ ]

class AccountInLine(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = "Accounts"
    

class Customize_user_admin(UserAdmin):
    inlines = (AccountInLine,)
    #list_display("username")
   

class CustomModelAdmin(admin.ModelAdmin):  
    
    def __init__(self, model, admin_site):
        self.search_fields = ['id']
        self.list_display = [field.name for field in model._meta.concrete_fields]
        # self.list_display = ([ field.name for field in  model._meta.concrete_fields if not field.many_to_many and not field.one_to_many ])
        # self.list_display = [self.get_products,]

        super(CustomModelAdmin, self).__init__(model, admin_site)


admin.site.unregister(User)
admin.site.register(User,Customize_user_admin)
admin.site.register(Category)
admin.site.register(Cmenue)
admin.site.register(Customer)
admin.site.register(Product,AdminReg)
admin.site.register(Order,CustomModelAdmin)
admin.site.register(OrderItem,CustomModelAdmin)
admin.site.register(ShippingAddress)






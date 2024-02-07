from django.db import models

# Create your models here.
from store.models import Product


class Cart():
    def __init__(self,request) :
        self.session = request.session
        
        
        #get the current session key if it exist
        cart = self.session.get('session_key')
        
        #if user is new creat new session 
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}                   
#make sure cart is available on all pages of site
        self.cart = cart 
           
    def add(self,product):
        product_id = str(product.id)
        
        #logic 
        if product_id in self.cart:
            self.remove(product)
                        
        else:
            self.cart[product_id] = {'price': str(product.price)}
            
        self.session.modified = True
        
    
    
    #get the length of item in cart 
    def __len__(self):
        return len(self.cart)
    
   
   
    def get_prods(self):
       #get ids from cart 
       product_ids = self.cart.keys()
       #use ids to lookup products in database model
       products = Product.objects.filter(id__in=product_ids)
       return products,product_ids
    def get_prods2(self):
       #get ids from cart 
       product_ids = self.cart.keys()
       #use ids to lookup products in database model
       #products = Product.objects.filter(id__in=product_ids)
       return product_ids
   
    def cart_delete(self,product):
        product_id = str(product.id)             
        cart = Cart(request.session)
        product = Product.objects.get(id=request.GET.get('id'))
        cart.remove(product)
        return HttpResponse("Removed")

   
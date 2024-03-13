from store.models import Product,Customer
from django.http import JsonResponse,HttpRequest,HttpResponse
import json
from django.contrib.auth.models import User
from django.shortcuts import render

class Cart():
    def __init__(self,request) :
        if request.user.is_authenticated:
            self.session = request.session       
            #get the current session key if it exist
            cart = self.session.get('session_key')     
            #if user is new creat new session 
            if 'session_key' not in request.session:
                cart = self.session['session_key'] = {}                   
            #make sure cart is available on all pages of site
            self.cart = cart 
        else:
            try:
                cart = json.loads(request.COOKIES['cart'])
                if cart is None :
                    cart = {}
                    print('cart is none')
            except:
                print('reach except init ')
                cart = {}
                # cart = json.loads(request.COOKIES['cart'])
            self.cart = cart
    def add_db(self,request,product,quantity):
        product_id = str(product) 
        product_qty = str(quantity)
        #logic 
        if product_id in self.cart:
            self.cart[product_id] = int(product_qty)
            print(self.cart)
            #self.cart.pop(product_id)                  
        else:
            self.cart[product_id] = int(product_qty)
            print(self.cart)
            #self.cart[product_id] = int(product_id)
            # self.cart[product_id] = {'price': str(product.price)}        
        if request.user.is_authenticated:
            print('USer',request.user)
            #TODO get current user 
            print("SELF",request.user.id)
            c_u = Customer.objects.filter(user__id=request.user.id)
            c_cart =str(self.cart)
            print(c_u,"USER")
            c_cart = c_cart.replace("\'","\"")
            c_u.update(old_c=c_cart)
            self.session.modified = True          
    def add(self,request,product,quantity):
        product_id = str(product.id) 
        product_qty = str(quantity)
        #logic 
        if product_id in self.cart:
            self.cart[product_id] = int(product_qty)
            print(self.cart)
            #self.cart.pop(product_id)                  
        else:
            self.cart[product_id] = int(product_qty)
            print(self.cart)
            #self.cart[product_id] = int(product_id)
            # self.cart[product_id] = {'price': str(product.price)}        
        if request.user.is_authenticated:
            print('USer',request.user)
            #TODO get current user 
            print("SELF",request.user.id)
            c_u = Customer.objects.filter(user__id=request.user.id)
            c_cart =str(self.cart)
            print(c_u,"USER")
            c_cart = c_cart.replace("\'","\"")
            c_u.update(old_c=c_cart)
            self.session.modified = True    

    #get the length of item in cart 
    def __len__(self):
        return len(self.cart)
    
   
    def get_prods(self):
       #get ids from cart 
       product_ids = self.cart.keys()
       #use ids to lookup products in database model
       products = Product.objects.filter(id__in=product_ids)
       return products 
    def get_prods2(self):
       #get ids from cart 
       product_ids = self.cart.keys()
       #use ids to lookup products in database model
       #products = Product.objects.filter(id__in=product_ids)
       return product_ids
    def get_quants(self):
        quantities = self.cart
        return quantities
    
    def delete(self,request,product,product_qty):
            product_id = str(product.id) 
            product_qty = int(product_qty)
            
            # if product_id in self.cart and product_qty <=0:
                # del self.cart[product_id]
            #logic 
            if product_id in self.cart:
                self.cart[product_id] = int(product_qty - 1)
                print('prodqI',product_id)
                if self.cart[product_id] <= 0 : 
                    del self.cart[product_id]  
                    print(self.cart)
                else:
                    print(self.cart)
                    print("still in cart ")
                    
                #self.cart.pop(product_id)
                # thing = self.cart
                # return thing
            else:
                print("elsepy")
                # self.cart[product_id] = {'id': str(product.id)}
                self.cart[product_id] = int(product_qty - 1 )
                # self.cart[product_id] -= 1 
                print(self.cart)
            if request.user.is_authenticated:
                print('US',request.user)
                print(self.cart)
                #TODO get current user 
                print("SELF",request.user.id)
                c_u = Customer.objects.filter(user__id=request.user.id)
                c_cart =str(self.cart)
                print(c_u,"USER")
                c_cart = c_cart.replace("\'","\"")
                c_u.update(old_c=c_cart)
                self.session.modified = True
                print(self.cart)

                # return HttpResponse("Removed")

    
    def update(self,request,product,quantity):
        product_id = str(product)
        product_qty = int(quantity)
        #get cart 
        ourcart = self.cart
        #update dic cart
        ourcart[product_id] = product_qty
        #self.session.modified = True
        thing = self.cart
        print(self.cart)
        if request.user.is_authenticated:
            print('US',request.user)
            #TODO get current user 
            print("SELF",request.user.id)
            c_u = Customer.objects.filter(user__id=request.user.id)
            c_cart =str(self.cart)
            print(c_u,"USER")
            c_cart = c_cart.replace("\'","\"")
            c_u.update(old_c=c_cart)
            self.session.modified = True
        return thing 
    
    def cart_total(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        quantities = self.cart
        total = 0 
        for key,value in quantities.items():
            #conver string to int to do math
            key = int(key)
            for product in products:
                if product.id == key :
                    total = total + (product.price * value)
        return total
        
    def get_itemq(self,product_id):
        product_id = str(product_id)
        quntities = self.cart
        for key,value in quntities.items():
            if str(key) == str(product_id):
                return value
    
    def cls (self,request):
        thing = self.cart
        thing.clear()
        if request.user.is_authenticated:
            print('US',request.user)
            self.session.modified = True
        return thing 
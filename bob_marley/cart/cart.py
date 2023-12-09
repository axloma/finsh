from store.models import Product
from django.http import JsonResponse,HttpRequest,HttpResponse

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
            pass
            #self.cart.pop(product_id)
                        
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
       return products 
    def get_prods2(self):
       #get ids from cart 
       product_ids = self.cart.keys()
       #use ids to lookup products in database model
       #products = Product.objects.filter(id__in=product_ids)
       return product_ids
   
    def delete(self,product):
            product_id = str(product.id) 
            #logic 
            if product_id in self.cart:
                self.cart.pop(product_id)
                            
            else:
                self.cart[product_id] = {'id': str(product.id)}
                
            self.session.modified = True
            return HttpResponse("Removed")
    
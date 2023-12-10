from django.shortcuts import render, get_object_or_404
from .cart import Cart
from store.models import Product
from django.http import JsonResponse,HttpRequest,HttpResponse
# Create your views here.


def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    ids = Cart(request)
    i = list(ids.get_prods2())
    i_dict =  ids.get_prods()
    i.sort()
    return render(request,"cart_summary.html",{'cart_products':cart_products,'i':i ,'i_dict':i_dict})


def cart_add(request):
    #get the cart 
    cart = Cart(request)
    #test for Post
    if request.POST.get('action') == 'post':
        #get data
        product_id = int(request.POST.get('product_id'))
        #Lookup product in db
        product = get_object_or_404(Product,id=product_id)
        
        #save to session
        cart.add(product=product)
        
        #get cart q 
        cart_quantity = cart.__len__()
        cart_item = list(cart.get_prods2())
        #return respose product info 
        # response = JsonResponse({'Product Name': product.name})
       #return cart quantity 
      
       
        response = JsonResponse({'qty': cart_quantity,'cart_item':cart_item})
        return response

    
    
    

def cart_delete(request):
    #get the cart 
    cart = Cart(request)
    #test for Post
    if request.POST.get('action') == 'post':
        #get data
        product_id = int(request.POST.get('product_id'))
        #Lookup product in db
        product = get_object_or_404(Product,id=product_id)
        
        #save to session
        cart.delete(product)
        
        #get cart q 
        cart_quantity = cart.__len__()
        # cart_item = cart.get_prods2()
        # return respose product info 
        # response = JsonResponse({'Product Name': product.name})
       #return cart quantity 
        response = JsonResponse({'qty':cart_quantity})
        return response



def cart_update(request):
    pass






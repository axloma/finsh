from django.shortcuts import render, get_object_or_404, redirect
from django.shortcuts import  get_object_or_404
from .cart import Cart
from store.models import *
from . utils import checkifo , checkemail
from django.http import JsonResponse,HttpRequest,HttpResponse
import datetime
import json
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
#    # from django.view.
# @csrf_exempt      
from django.contrib import messages


def cart_summary(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        #TODO query objects or create it 
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        items = order.orderitem_set.all()#TODO get all order from child
        cartItems = order.get_cart_items
        cart = Cart(request)
        cart_products = cart.get_prods()
        #get all keys in cart 
        i = list(cart.get_prods2())
        i.sort()
        quantities = cart.get_quants 
        totals = cart.cart_total()
        #for movie card 
        mx = serializers.serialize("json", cart_products,cls=DjangoJSONEncoder)       
        context = {'cart_products':cart_products,'i':i ,'quantities':quantities,
                'items':items,'order':order,'cartItems':cartItems,'totals':totals , 'mx':mx        }
        print('cart',cart)
        print(type(cart))
    else:
        # get the cookie and parse it to python dictionary for unauthenticated user
        try:          
            #cart = json.loads(request.COOKIES['cart'])
            cart = Cart(request)
            #cart = Cart(request)
            print('cart',cart)
            print(type(cart))
            cart_products = cart.get_prods()
            i = list(cart.get_prods2())
            #items = []    
            #order = {'get_cart_total':0,'get_cart_items':0}
            # cartItems = ['order.get_cart_items']
            #cartItems = order['get_cart_items']
            #for i in cart:
            #    cartItems += cart[i]['quantity']     
            mx = serializers.serialize("json", cart_products,cls=DjangoJSONEncoder) 
            quantities = cart.get_quants      
            totals = cart.cart_total()
            context = {'cart_products':cart_products,'totals':totals,'i':i,'mx':mx,'quantities':quantities}
            print("reach tryy")
        except:
            #create cart cookie if not exist 
             print("reach except summry")
             cart = json.loads(request.COOKIES['cart'])
             response = render(request, 'home.html', {})
            #  response.set_cookie('cart', {})
             response.set_cookie('cart', cart)   
             return response
        #return render(request,"cart_summary.html",context)
    return render(request,"cart_summary.html",context)
def checkout(request):
    print("GO")
    cart = Cart(request)
    cart_products = cart.get_prods()
    #get all keys in cart 
    i = list(cart.get_prods2())
    i.sort()          
    mx = serializers.serialize("json", cart_products,cls=DjangoJSONEncoder) 
    totals = cart.cart_total()      
    context = {'page':"CHECKOUT",'mx':mx,'i':i,'totals':totals }
    return render(request,"checkout.html",context)

    
    

# @csrf_exempt
def cart_add(request):
    #get the cart 
    cart = Cart(request)
    #test for Post
    print(cart.__len__(),"QUN")
    if request.POST.get('action') == 'post':
        #get data
        try:    
            product_id = int(request.POST.get('product_id'))
            product_qty = int(request.POST.get('product_qty'))
            print(product_id,"ID","QNT",product_qty)
            #TODO make sure product qunt exist 
            if product_qty == '' or product_qty == None:
                #product_qty = '1'
                print("product quant error adding")
            #TODO check for product id 
            elif  product_id == '':
                print("product id error adding")
            #Lookup product in db
            product = get_object_or_404(Product,id=product_id)
            if not product :
                print("error creating product")
            #save to session
            cart.add(request,product=product,quantity=product_qty)
            #get cart q length
            cart_quantity = cart.__len__()
            cart_item = list(cart.get_prods2())
            #return respose product info 
            # response = JsonResponse({'Product Name': product.name})
        #return cart quantity   
            response = JsonResponse({'qty': cart_quantity,'cart_item':cart_item})
            print('cartadd',cart.__len__())
            print("cart_Q",cart_quantity)
            return response
        except:
            print("REACH except in adding ")
        
def cart_delete(request):
    #get the cart 
    cart = Cart(request)
    #test for Post
    if request.POST.get('action') == 'post':
        #get data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        #Lookup product in db
        product = get_object_or_404(Product,id=product_id)       
        #save to session
        # cart.delete(request,product)
        cart.delete(request,product,product_qty)
        #get cart q 
        cart_quantity = cart.__len__()
        # cart_item = cart.get_prods2()
        # return respose product info 
        # response = JsonResponse({'Product Name': product.name})
       #return cart quantity 
        #get Item qunt
        pq = cart.get_itemq(product_id)
        response = JsonResponse({'qty':cart_quantity,'pq':pq})
        return response
    
def cart_update(request):
      cart = Cart(request)
      if request.POST.get('action') == 'post':
        #get data
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))  
        cart.update(request,product=product_id,quantity=product_qty)
        response = JsonResponse({'qty':product_qty})
        return response
    
@csrf_exempt    
def processOrder(request):
    # create transiction id 
    transaction_id = datetime.datetime.now().timestamp()
    # parse data after stringify it 
    data = json.loads(request.body)
    cart = Cart(request)
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer,status=False)
        total = float(data['form']['total'])
        order.transaction_id = transaction_id
        # check if total process from fron't end is the same in backend
        # if total == order.get_cart_total:
        #     order.status = True
        # order.save()
        if float(total) == float(cart.cart_total()):
            order.status = True
        order.save()
        # insert data into shipping address
        if order.status == True:
            ShippingAddress.objects.create(
                customer=customer,order=order,address=data['form']['address'],
                city=data['form']['city'],state=data['form']['state'],zipcode=data['form']['zipcode'], phone=data['form']['phone'],
                
            )   
        #clear cart 
        # cart_quantity = cart.__len__()
        cart.cls(request)
    else:
        cus = data['form']['email']
        cusn = data['form']['name']
        address = data['form']['address']
        city = data['form']['city']
        phone = data['form']['phone']
        state=data['form']['state']
        zipcode=data['form']['zipcode']
        #check empty field                         
        checked,d_m = checkifo(request,cusn,cus,address,city,phone)
        if not checked :
            errorx = {"error":"EMPITY FIELD","MSG":d_m}
            res = JsonResponse(errorx,safe=False)
            return res  #redirect('cart_summary')
        #check email validation
        checkEmail,d_m = checkemail(request,cus)
        if not checkEmail:
            print("NOT VALID EMAIL ")
            errorx = {"error":"EMAIL_E","MSG":d_m}
            res = JsonResponse(errorx,safe=False)
            return res 
        # d_m = []

        # for message in messages.get_messages(request):
        #     d_m.append({
        #         "level": message.level,
        #         "message": message.message,
        #         "extra_tags": message.tags,
        # })
        
            # return redirect('home')
        
            
            
        customer , created = Customer.objects.get_or_create(email=cus,first_name=cusn)
        # customer.name = cusn
        customer.save()
        order , created = Order.objects.get_or_create(customer=customer,status=False)
        total = data['form']['total']
        order.transaction_id = transaction_id
        # check if total process from fron't end is the same in backend
        print('total java',total)
        print('typeof java',type(total))
        print('typeof cart total',type(cart.cart_total()))
        print('total cart',cart.cart_total())
        if float(total) == float(cart.cart_total()):
            order.status = True
        
        # order.save()
        
        # insert data into shipping address
        if order.status == True:
            ShippingAddress.objects.create(
                customer=customer,order=order,address=address,
                city=city,state=state,zipcode=zipcode,
                phone=phone,
            )
            # ShippingAddress.objects.create(
            #     customer=customer,order=order,address=data['form']['address'],
            #     city=data['form']['city'],state=data['form']['state'],zipcode=data['form']['zipcode'],
            #     phone=data['form']['phone'],
            # )
        ix = list(cart.get_prods2())
        #add order item for unauthentic user 
        for i in ix :
           q = cart.get_itemq(i)
           p = Product.objects.get(id=i)
           orderitem = OrderItem.objects.create(product=p,order=order,quantity=q)
           orderitem.save()
        order.quantity = order.get_cart_items
        order.save()
        print("cartbefore",cart.__len__())
        cart.cls(request)
        print("ctafter",cart.__len__())
    return JsonResponse('item was addeed',safe=False)





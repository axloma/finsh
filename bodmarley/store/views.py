# import queue
from queue import Queue
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import LoginReg ,Update_user_form
from django import forms
from .models import *
from cart.cart import Cart
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.db.models import Q
import json
from django.contrib.auth.models import User
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from . utils import MV_HOLD

# # from django.view.
# @csrf_exempt
def category(request,foo):
    try:
        #utils function return dict category
        con = MV_HOLD(request,"CATEGORY",foo)
        context ={'products':con["products"] , 'category':con["category"], "categorys":con['categorys'] ,'i':con['i'] ,'mx':con["mx"],'page':con['page']}
        return render(request,'category.html',context )
    except:
        messages.error(request,"wrong cat")
        return redirect('home')
    
def product(request,pk):
    con = MV_HOLD(request,"PRODUCT",pk)
    return render(request,'product_view.html', {"product":con["product"] ,"i":con['i'],
                                                'quantities':con['quantities'],'mx':con["mx"],'page':con['page']})
# @csrf_exempt
def home(request):
    products_s = ()
    #for search 
    if request.POST.get('action') == 'post':
        #get data
        product_str = str(request.POST.get('search'))
        products_n = Product.objects.filter(name__icontains=product_str)
        products_s =  list( products_n.values())     
        response = JsonResponse({'product_s':products_s})      
        return response
    con = MV_HOLD(request,"HOME")
    context = {'products':con["products"],'categorys':con["categorys"],'i':con["i"],
               'i_dict':con["i_dict"] ,'products_s':products_s,'mx':con["mx"],'quantities':con["quantities"],"page":con["page"]}
    return render(request, 'home.html',context)
   
def about(request):
    c_u = User.objects.get(id=request.user.id)
    c_u_c , created = Customer.objects.get_or_create(user=request.user)
    u_form_u =  Update_user_form(request.POST or None , instance=c_u_c)
    context = MV_HOLD(request,"ABOUT")
    return render(request, 'about.html',{'form':u_form_u,'page':context["page"],'mx':context["mx"]})


# @csrf_exempt
def reg_U(request): 
    if request.user.is_authenticated:
        return redirect('about')
    i = "NONE"
    mx = "NONE"
    form = LoginReg()
    if request.method == "POST":
        form = LoginReg(request.POST)
        if form.is_valid():
            # create customer when user is created 
            # customer , created = Customer.objects.get_or_create(email=[],first_name=cusn)
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            f_n = form.cleaned_data["first_name"]
            l_n = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            phone = form.cleaned_data["phone"]
            #login user 
            user = authenticate(username=username,password=password)
            #create customer
            customer =  Customer.objects.create(user=user,first_name=f_n,last_name=l_n,phone=phone,email=email,password=password)
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"error")
            return redirect('register')
    return render(request, 'register.html',{"form":form,'i':i,"mx":mx})

def update_u_info(request):
    con = MV_HOLD(request,"UPDATE_USER")
    if request.user.is_authenticated:
        c_u = User.objects.get(id=request.user.id)
        # GET CUS OR CREATE IT 
        c_u_c , created = Customer.objects.get_or_create(user=c_u)
        u_form = Update_user_form(request.POST or None , instance=c_u_c)
        u_form_u =  Update_user_form(request.POST or None , instance=c_u)
        u_form.fields["username"].initial = request.user.username
        if u_form.is_valid():
            u_form_u.save()
            u_form.save()
            login(request,c_u)
            messages.success(request,"UPDATED SUCCESSFULLY")
            return redirect('about')
        return render(request, 'updateU.html',{'form':u_form,'page':con["page"],'mx':con["mx"],})
    else:
        messages.success(request,"LOGIN FIRST IDIOT")
        return redirect('home')
              
     
    

def logout_U(request):
    logout(request)
    return redirect('home')


def login_U(request):
    #return render(request, 'login_P.html',{})
    if request.user.is_authenticated:
        return redirect('about')
    else:     
        con = MV_HOLD(request,"LOGIN")
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["pass"]
            user = authenticate(request, username=username,password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request,"wrong credential")
                return redirect('login_U')
        else:
            return render(request,'login_P.html',{'page':con["page"],"mx":con["mx"],'i':con['i']})

# for authenticated user 
def updateItem(request):
    # parse data came from json
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    qt = data["qt"]
    print('p',productId )
    #get logged in cust
    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer,status=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order,product=product)
    if action == 'add':         
        # print(orderItem.quantity)
        # orderItem.quantity = (orderItem.quantity + 1)
        #   orderItem.quantity = (orderItem.quantity + int(qt))
        orderItem.quantity =  int(qt)
        order.Product = product
        #   order.quantity = int(qt)
        # order.quantity = order.get_cart_items
    elif action == 'remove':
        order.delete()
        # orderItem.quantity = (orderItem.quantity - 1 )
        orderItem.quantity = (orderItem.quantity - int(qt)) 
    if orderItem.quantity <= 0:
        orderItem.delete()       
    orderItem.save()
    print("I",order.get_cart_items)
    order.quantity = order.get_cart_items
    order.save()

    return JsonResponse('item was added',safe=False)
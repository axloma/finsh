# import queue
from queue import Queue
from django.shortcuts import render,redirect,get_object_or_404
from .models import Product
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import LoginReg
from django import forms
from .models import Product, Category
#from cart.models import Cart
from cart.cart import Cart
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.db.models import Q
from django.core import serializers

# from django.view.

def category(request,foo):
    # c_name = c_name.replace('-',' ')
    # get category 
    try:
        ids = Cart(request)
        i = list(ids.get_prods2())
        i_dict =  ids.get_prods()
        i.sort()
        category = Category.objects.get(name=foo)
        categoryx = Category.objects.get(name=foo)
        categorys = Category.objects.all()
        products = Product.objects.filter(Category=category)
        return render(request,'category.html', {'products':products , 'category':category , "categorys":categorys ,"categoryx":categoryx,'i':i})
    except:
        messages.error(request,"wrong cat")
        return redirect('home')
    
    
    
def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product_view.html',{"product":product})

# Create your views here.
def home(request):
    products = Product.objects.all()
    categorys = Category.objects.all()
    ids = Cart(request)
    i = list(ids.get_prods2())
    i_dict =  ids.get_prods()
    i.sort()
    products_l = list()
    products_s = ()
    if request.POST.get('action') == 'post':
        #get data
        product_id = str(request.POST.get('search'))
        products_id = 'V'
        products_id2 =request.POST.get('search')
        product_str = str(products_id2)
        #Lookup product in db
        # product = get_object_or_404 (Product,id=product_id)
        # products = Product.objects.filter(Q(name__icontains=product_str) | Q(id=int(product_id)))
        products_n = Product.objects.filter(name__icontains=product_str)
        products_s =  list( products_n.values())
        
        # product = Product.objects.filter(id=product_id)
        # products_l = list()
        # p_d = Product.objects.filter(id=product_id)
        for name in products_n:
              products_l.append(name.name)
              products_l.append(name.id)
     
            
            
        # product_name = product.name
        #get cart q 
        #cart_quantity = cart.__len__()
       # cart_item = list(cart.get_prods2())
        #return respose product info 
        # response = JsonResponse({'Product Name': product.name})
        # response = JsonResponse({'product':product_name,'products_l':products_l})     
        response = JsonResponse({'products_l':products_l,'product_s':products_s})
        # qs_json = serializers.serialize('json', products_s)
        # return HttpResponse(qs_json, content_type='application/json'),response
        # context = {'products':products,'categorys':categorys,'i':i ,'i_dict':i_dict ,'response':response};
        return response
    context = {'products':products,'categorys':categorys,'i':i ,'i_dict':i_dict ,'product_l':products_l,'products_s':products_s}
    return render(request, 'home.html',context)
   








def about(request):
    return render(request, 'about.html',{})

def reg_U(request): 
    if request.user.is_authenticated:
        return redirect('about')
    form = LoginReg()
    if request.method == "POST":
        form = LoginReg(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            #login user 
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"error")
            return redirect('register')
    return render(request, 'register.html',{"form":form})


def logout_U(request):
    logout(request)
    return redirect('home')

def login_U(request):
    #return render(request, 'login_P.html',{})
    if request.user.is_authenticated:
        return redirect('about')
    else:
            
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
            return render(request,'login_P.html',{})


# def logout_U(request):
#     logout(request)
#     return redirect('home')


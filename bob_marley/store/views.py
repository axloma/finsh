from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import LoginReg
from django import forms
from .models import Product, Category
#from cart.models import Cart
from cart.cart import Cart


def category(request,foo):
    # c_name = c_name.replace('-',' ')
    # get category 
    try:
        category = Category.objects.get(name=foo)
        categoryx = Category.objects.get(name=foo)
        categorys = Category.objects.all()
        products = Product.objects.filter(Category=category)
        return render(request,'category.html', {'products':products , 'category':category , "categorys":categorys ,"categoryx":categoryx})
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
    return render(request, 'home.html',{'products':products,'categorys':categorys,'i':i ,'i_dict':i_dict})

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


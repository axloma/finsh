# import queue
from queue import Queue
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from .forms import LoginReg ,Update_user_form ,Change_p
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
from . utils import MV_HOLD,lives
from .models import Product
from decimal import Decimal
from decimal import Context, Decimal, getcontext

from django.core.paginator import Paginator

# # from django.view.
# @csrf_exempt
def category(request,foo):
    try:
        # products_s = ()
        #for search 
        if request.POST.get('action') == 'post':
            return lives(request)
        #     #get data
        #     product_str = str(request.POST.get('search'))
        #     products_n = Product.objects.filter(Q(name__icontains=product_str) | Q(description__icontains=product_str))
        #     products_s =  list( products_n.values())     
        #     response = JsonResponse({'product_s':products_s})      
        #     return response
        #utils function return dict category
        
        con = MV_HOLD(request,"CATEGORY",foo)
        context ={'products':con["products"] , 'category':con["category"], "categorys":con['categorys'] ,'i':con['i'] ,'mx':con["mx"],'page':con['page'],'item':con['item'],'nums':con['nums']}
        return render(request,'category.html',context )
    except:
        messages.error(request,"wrong cat")
        return redirect('home')


def search(request):
    if request.method == 'POST':
         searched = request.POST['search']       
         searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))
         mx = serializers.serialize("json", searched,cls=DjangoJSONEncoder)
         if not searched:
                messages.error(request,"nothing  try again ")
         return render(request,'search.html',{'searched':searched,'mx':mx})        
    return render(request,'search.html',{})     


def C_menue(request,foo):
    try:
        #for search 
        if request.POST.get('action') == 'post':
            return lives(request)
          
        #utils function return dict category
        con = MV_HOLD(request,"CATEGORY_M",foo)
        context ={'products':con["products"] , 'category':con["category"], "categorys":con['categorys'] ,'i':con['i'] ,'mx':con["mx"],'page':con['page'],'item':con['item'],'nums':con['nums']}
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

    
    first = Product.objects.first()
    print(first.id,"ID")
    print(first.name,"NAME")

    products_s = ()
    #for search 
    if request.POST.get('action') == 'post':
        #get data
        product_str = str(request.POST.get('search'))
        products_n = Product.objects.filter(name__icontains=product_str)
        products_s =  list( products_n.values())     
        response = JsonResponse({'product_s':products_s})      
        return response
    try:   
        con = MV_HOLD(request,"HOME")
        context = {'products':con["products"],'categorys':con["categorys"],'i':con["i"],
                'i_dict':con["i_dict"] ,'products_s':products_s,'mx':con["mx"],'quantities':con["quantities"],"page":con["page"],'item':con['item'],'nums':con['nums']}
        return render(request, 'home.html',context)
    except:
           return render(request, 'home.html')
    # return render(request, 'home.html',context)
   
def about(request):
    c_u = User.objects.get(id=request.user.id)
    c_u_c , created = Customer.objects.get_or_create(user=request.user)
    u_form_u =  Update_user_form(request.POST or None , instance=c_u_c)
    u_form_u.fields["username"].initial = request.user.username
    #disable text
    for f in u_form_u.fields.values():
            f.widget.attrs['disabled'] =True

    # u_form_u['username'] = c_u.username
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
        messages.success(request,"LOGIN FIRST ")
        return redirect('home')
              
def update_u_p(request):
    con = MV_HOLD(request,"UPDATE_Password")
    if request.user.is_authenticated:
        c_u = request.user 
        if request.method == "POST":
            form = Change_p(c_u,request.POST)
            if form.is_valid():
                form.save()
                login(request,c_u)
                messages.success(request,"UPDATED SUCCESSFULLY")
                return redirect('update_u_info')
            else:
                for error in list(form.errors.values()): #TODO get django form error And convert it to list
                        messages.success(request,error)#PASS ERROR in msgs
                        return redirect('update_p')
        else:
            form = Change_p(c_u)
            #return render(request,'update_p.html',{'form':form,'page':con["page"],'mx':con["mx"]})
            return render(request, 'updateU.html',{'form':form,'page':con["page"],'mx':con["mx"],})
    else:
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
                #TODO get c cus
                c_cus = Customer.objects.get(user__id=request.user.id)
                print(c_cus)
                old_c = c_cus.old_c
                if old_c:
                    conv_c = json.loads(old_c)
                    cart = Cart(request)
                    for key,value in conv_c.items():
                        cart.add_db(request,product=key,quantity=value)

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

def add_p(request):
    #insert from scrapy 
    p = Product
    # with open('disposable.json','r') as file:
    # with open('ovsegdispos.json','r') as file:   
    # with open('ovsegdl.json','r') as file: 
    # with open('ovsegmtl.json','r') as file:       
    # with open('ovsegvape.json','r') as file:    
    # with open('ovsegsalt.json','r') as file:
    # with open('ovsegEdl.json','r') as file:  
    # with open('ovsegEmtl.json','r') as file:          
    # with open('ovsegEsalt.json','r') as file:
    # with open('ovsegtank.json','r') as file:  
    
    allp = Product.objects.all()
    ls =  []
    ct = "PRIMUM_liquid"
    cm = "premuim_a"
    for i in allp:
        ls.append(i.name)
    print(ls)
    # with open('coil.json','r') as file:            
    # with open('elclandispos.json','r') as file: 
    # with open('elclanpod.json','r') as file:
    # with open('media/images_folder/kit/elclankit.json','r') as file:     
    # with open('media/images_folder/coil/elclancoil.json','r') as file:
    # with open('media/images_folder/mod/elclanmod.json','r') as file:
    # with open('media/images_folder/tank/elclantank.json','r') as file:
    # with open('media/images_folder/tools/elclantools.json','r') as file: 
    with open('media/images_folder/prem/elclanprem.json','r') as file:     
                
            data = json.load(file)
            #print(len(data['name']))
            #name = list(data['name'])
    try:
        for i in data :
            name = i['name']
            price = str(i['price']).replace(',','')
            #FOR ELCLAN dispos
            newprice = str(i['newprice']).replace(',','').replace('جنيه','')
            disc = str(i['disc'])
            # img = 'images_folder/'+i['img_path']
            # img = 'images_folder/'+i['img_path']
            # img = 'images_folder/kit/'+i['img_path']
            # img = 'images_folder/coil/'+i['img_path']
            img = 'images_folder/prem/'+i['img_path']
            ##########
            link = str(i['link'])
            # im = 'images_folder/'+i['images'][0]['path']
            # nic = str(i['NICOTINE'])
            # ndisc = name + "\n" + "NIC: " + nic
            # nprice = list(i['price'])
            # xp = ""
            # for ip in nprice:
            #     print(ip,"PRI")
            #     ipx = ip + "-"
            #     xp += ipx
            #     print(xp)
            # newdisc = name +'\n'+ xp
            # print(newdisc)
            #TODO make sure product not already exist
            if name in ls :
                print("NAME ALREADY EXIST",name)
                ps = Product.objects.filter(name=name,description=disc)
                print(ps.count(),"COUNT")
                print(ps)
                if ps:
                    if(ps.count() > 0):
                        for s in ps :
                            print(s.price,"PRODUCT PRICE ")
                            print(s.description,"PRODUCT DISC ")
                            print(s.Category_M,"CAT")
                            print(s.Category,"CATe")
                            if name == s.name and Decimal(newprice) == s.price and disc == s.description:
                                print("PRODUCT ALREADY IN DB IDIOT")
      
                else:
                    print("IT NOT THE SAME ")
                    liquid = Category.objects.get(name=ct)
                    cmenu = Cmenue.objects.get(name=cm)
                    
                    p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)             
            else:
                # price2 = price
                # price2 = price2[:8]
                # dp = Decimal(price2)
                # print(price2,"PRICE2")
                # d_price = float(price2)
                
                # print(im,"IMAGR_PATHE")
                # newp = price[:8]
                # newp = price2[:5]
                # newp = str(newp)
                # newp = xp[:6]
                # print("NEWP",newp)
                # print(im)
                # print(link,"LINK")
                # pR= str(i['price'].replace(',','.'))
                # pr = pR[:5].strip()
                # pR = Decimal(pR[:5])
                # newp = Decimal(price2)
                # print("PRICENOW")
                # print(getcontext().prec)
                # print(newp.quantize(Decimal('1000.000'))) 
                # newp = newp.quantize(Decimal('100.000'))
                # print(d_price)
                # liquid = Category.objects.get(name="VAPE")
                # liquid = Category.objects.get(name="PRIMUM_liquid")   
                # liquid = Category.objects.get(name="liquid")   
                # cmenu = Cmenue.objects.get(name="E_liquid")
                # cmenu = Cmenue.objects.get(name="MTL_liquid")
                # cmenu = Cmenue.objects.get(name="SALT_Liquid")
                # cmenu = Cmenue.objects.get(name="TANK")
                # cmenu = Cmenue.objects.get(name="Accessories")
                # cmenu = Cmenue.objects.get(name="coils-cartridges")
                # cmenu = Cmenue.objects.get(name="disposable")
                # cmenu = Cmenue.objects.get(name="POD")
                # cmenu = Cmenue.objects.get(name="Accessories")

                liquid = Category.objects.get(name=ct)
                cmenu = Cmenue.objects.get(name=cm)

                p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)

                # cmenu = Cmenue.objects.get(name="kit")
                # liquid = Category.objects.get(name="liquid")
                # p.objects.create(name=name,price=dp,image=im,description=ndisc,Category=liquid,outsidelink=link,Category_M=cmenu)
                # p.objects.create(name=name,price=dp,image=im,description=name,Category=liquid,outsidelink=link,Category_M=cmenu)
                # p.objects.create(name=name,price=dp,image=im,description=name,Category=liquid,outsidelink=link,Category_M=cmenu)
                # p.objects.create(name=name,price=newp,image=im,description=name,Category=liquid,outsidelink=link)
                # p.objects.create(name=name,price=newp,image=im,description=name,Category=liquid)
                # p.save()
                print("created")
                # print(newp)
    except  :
        print("ERRROR")
        
    return render(request,'add_product.html',{'name':name,'price':price,'im':img})

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
from django.views.generic import View,TemplateView
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
import requests
from django.core.paginator import Paginator
import re
import time
# # from django.view.
# @csrf_exempt
def category(request,foo):
    try:
        # products_s = ()       
        #utils function return dict category
        con = MV_HOLD(request,"CATEGORY",foo)
        pg = con['page']
        #for search 
        if request.POST.get('action') == 'post':
            return lives(request,foo,pg)
              
        context ={'products':con["products"] , 'category':con["category"],
                "categorys":con['categorys'] ,'i':con['i'] ,'mx':con["mx"],
                'page':con['page'],'item':con['item'],'nums':con['nums'],
                'title':con['title']  }
        return render(request,'category.html',context )
    except:
        messages.error(request,"wrong cat")
        return redirect('home')

class Search(View):
    searchex = ""
    # request = ''
    def __init__(self,*args, **kwargs):
        super().__init__(**kwargs)
        # con = MV_HOLD(self.request,"SEARCH",kwargs.get('np'))
    
    def get(self,*args,**kwargs): 
        con = MV_HOLD(self.request,"SEARCH",kwargs.get('np'))
        sfor = self.request.GET.get('sfor')
        print(sfor,"SFOR")
        limit = kwargs.get('np')
        xlimit = limit -6
        searched = list(Product.objects.values().filter(Q(name__icontains=sfor) | Q(description__icontains=sfor))[xlimit:limit])
        ssize = list(Product.objects.values().filter(Q(name__icontains=sfor) | Q(description__icontains=sfor)))
        # val = Product.objects.values().get(id=149)
        mxlen = True if limit >= len(ssize) else False
        print(len(ssize),"MX")
        return JsonResponse({'data':searched,'mxl':mxlen},safe=False)            
    def post(self,*args,**kwargs):
        con = MV_HOLD(self.request,"SEARCH",kwargs.get('np'))
        searched = self.request.POST['search'] 
        self.searchex = searched      
        searched = Product.objects.filter(Q(name__icontains=searched) | Q(description__icontains=searched))[:15]
        mx = serializers.serialize("json", searched,cls=DjangoJSONEncoder)        
        if not searched:
                messages.error(self.request,"nothing  try again ")
        con = MV_HOLD(self.request,"SEARCH",kwargs.get('np'))
        return render(self.request,'search.html',{'searched':searched,'mx':mx,'serchfor':self.searchex,'i':con['i'],'page':con['page'],'quantities':con['quantities']})  

   
def C_menue(request,foo):
    try:
        #utils function return dict category      
        #for search               
        con = MV_HOLD(request,"CATEGORY_M",foo)
        pg = con['page']
        if request.POST.get('action') == 'post':
            return lives(request,foo,pg)            
        context ={'products':con["products"] , 'category':con["category"], 
                  "categorys":con['categorys'] ,'i':con['i'] ,'mx':con["mx"],
                  'page':con['page'],'item':con['item'],'nums':con['nums'],'title':con['title']}
        return render(request,'category.html',context )
    except:
        messages.error(request,"wrong cat")
        return redirect('home')  
    
def product(request,pk):
    con = MV_HOLD(request,"PRODUCT",pk)
    p = Product.objects.get(id=pk)
    images = P_IMG.objects.filter(product=p)
    imagesx = serializers.serialize("json", images,cls=DjangoJSONEncoder)
    # trypre = Product.objects.prefetch_related('p_img_set').all()#TODO get all product of imags 
    hb=Product.objects.all().prefetch_related('p_img_set').get(id=p.id) #TODO get product according prefetch
    trypre = P_IMG.objects.select_related('product').all()#TODO get all product of imags 
    val = Product.objects.values().get(id=pk)
    print(trypre[0].product,"TSELECTRELATED")
    print(hb.p_img_set.all(),"HHHHB")
    print("VALUES",val)
    print("PRODUCT",p)
    # print(d[2])
    context = {"product":con["product"] ,"i":con['i'],
              'quantities':con['quantities'],'mx':con["mx"],
             'page':con['page'],'images':images,'imagesx':imagesx,'title':con['title']}
    return render(request,'product_view.html',context )
# @csrf_exempt
def home(request):    
    products_s = ()
    try:   
        con = MV_HOLD(request,"HOME")
        pg = con['page']
        if request.POST.get('action') == 'post':
            return lives(request,pg,pg)
        context = {'products':con["products"],'categorys':con["categorys"],'i':con["i"],
                'i_dict':con["i_dict"] ,'products_s':products_s,'mx':con["mx"],
                'quantities':con["quantities"],"page":con["page"],'item':con['item'],
                'nums':con['nums'],'title':con['title']}
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
    return render(request, 'about.html',{'form':u_form_u,'page':context["page"],'mx':context["mx"],'title':"ABOUT"})


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
            # messages.error(request,"error")
            return render(request, 'register.html',{"form":form,'i':i,"mx":mx})
            # return redirect('register')
    return render(request, 'register.html',{"form":form,'i':i,"mx":mx,'title':'REGISTER'})

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
        return render(request, 'updateU.html',{'form':u_form,'page':con["page"],'mx':con["mx"],'title':'UPDATE_INFO'})
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
            return render(request,'login_P.html',{'page':con["page"],"mx":con["mx"],'i':con['i'],'title':'LOGIN'})

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

##########add product 
def add_p(request):
    #insert from scrapy 
    p = Product 
    allp = Product.objects.all()
    print(allp.count(),"NUMP")
    ls =  []
    ct = "SMOKING"
    cm = "SHISHA"
    cat = Category.objects.get(name=ct)
    cmenu = Cmenue.objects.get(name=cm,Category=cat)
    jsonfile = "media/images_folder/mo3ezshysha/mo3ezshysha.json"
               #media/images_folder/amazonaccess/amazonacess.json
    imgf = 'media/images_folder/mo3ezshysha/proi/product_img.json'
    imgfolder = '/images_folder/mo3ezshysha/proi/'
    for i in allp:
        ls.append(i.name)
    # print(ls)
    listimg = []
    with open(jsonfile,'r') as file:           
            data = json.load(file)
            #print(len(data['name']))
            #name = list(data['name'])
    with open(imgf,'r') as imgfile:
            imgdata = json.load(imgfile)
            for i in imgdata:
                dicimg = {}
                dicimg['link'] = i['link']
                dicimg['images'] = i['images']
                # time.sleep(5)
                print("IMGAGES",dicimg['images'])
                listimg.append(dicimg)
    try:
        for i in data:
            name = str(i['name']).strip()
            disc = str(i['disc']).strip()
            # price = str(i['price']).replace(',','')
            # ٣٬٥٥٠ جنيه
            price = str(i['price']).replace(',','').replace('EGP','').replace('جنيه','').replace('٬','')

            dp = Decimal(price)           
            print(dp,"PRIcE")
            ndp = dp + dp * 10 /100 
            if dp >= 2000 :
                ndp = dp + dp * 5 /100 
            # ndp = dp + dp * 10 /100 
            ndp = Decimal(ndp)
            print(ndp,"nPRIcE")
            proimages = []
            ##########
            link = str(i['link']).strip()

            for l in listimg :
                if link == l['link']:
                    proimages = l['images'] 
                    print(link,"LINK",proimages,"IMGAGES")
            # im = imgfolder+i['fmg']
            im = imgfolder+proimages[0]
            print(im,"im")
            #CHECK IF PRO has smg
            try:
                simg = imgfolder+i['simg']
                print(simg,"SMG")
            except:
                simg = ""
                print(simg,"SMGE")

            #TODO make sure product not already exist
            if name in ls  :
                print("NAME ALREADY EXIST",name)
                ps = Product.objects.filter(name=name,description=disc,outsidelink=link)
                print(ps.count(),"COUNT")
                print(ps)
                if ps:
                    if(ps.count() > 0):
                        for s in ps :
                            print(s.price,"PRODUCT PRICE ")
                            print(s.description,"PRODUCT DISC ")
                            print(s.Category_M,"CAT")
                            print(s.Category,"CATe")
                            print(len(ps),"PSLEN")
                            # time.sleep(2)
                            # if name == s.name and ndp == s.price  and disc == s.description and s.outsidelink == link  :
                            if name == s.name  and disc.strip() == s.description.strip() and s.outsidelink.strip() == link.strip()  :
                             
                                print("PRODUCT ALREADY IN DB IDIOT")

                            else:
                                print("IT NOT THE SAME ",i['id'])
                                time.sleep(2)
                                # prod = p.objects.create(name=name,price=ndp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)

                                # p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)
            else:
                try:
                    print("REACH ADD PROD")
                    prod = p.objects.create(name=name,price=ndp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)
                    for img in proimages:
                        im = imgfolder+ str(img)
                        P_IMG.objects.create(product=prod,image=im)

                    print("created",i['id'])
                    # time.sleep(1)
                except Exception as ex:
                    print("ERORO WITH",ex)
                # print(newp)
    except  Exception as error:
        # print(newprice,"NP")
        print("ERRROR",error)
    
    return render(request,'add_product.html',{'name':name,'price':price,'im':im})
def modifyprice():
     ct = "PRIMUM_liquid"
     cm = "PSALT_Liquid"
    #  ct = "VAPE"
     cm = "ACCESSORIES"
     cat = Category.objects.get(name=ct)
     ps = Product.objects.filter(Category=cat)
     for s in ps :
         print(s.name,s.price)
         ndp = s.price + s.price * 10 /100 
         if s.price >= 2000 :
             ndp = s.price + s.price * 5 /100 
             print("HIGHER")
         print(ndp)
         s.price = ndp
         s.save()
         print(s.name,"MODIFIED")

def modifydisc():
    ct = "SMOKING"
    cm = "SHISHA"
    cat = Category.objects.get(name=ct)
    ps = Product.objects.filter(Category=cat)
    jsonfile = "media/images_folder/mo3ezshysha/mo3ezshysha.json"
    with open(jsonfile,'r') as file:           
            data = json.load(file)
    for i in data:
        for s in ps:
            if i['link'] == s.outsidelink:
                s.name = i['disc']
                s.save()
    

# modifyprice()
# modifydisc()

def add_p1(request):
    #insert from scrapy 
    p = Product 
    allp = Product.objects.all()
    print(allp.count(),"NUMP")
    ls =  []
    ct = "SMOKING"
    cm = "melliferous-معسل"
    cat = Category.objects.get(name=ct)
    cmenu = Cmenue.objects.get(name=cm,Category=cat)
    jsonfile = "media/images_folder/mo3ezmazaya/mo3ezmazaya.json"
               #media/images_folder/amazonaccess/amazonacess.json
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    # imgfolder = '/images_folder/mo3ez/proi/'
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    imgfolder = '/images_folder/mo3ezmazaya/'

    for i in allp:
        ls.append(i.name)
    # print(ls)
    listimg = []
    with open(jsonfile,'r') as file:           
            data = json.load(file)
            #print(len(data['name']))
            #name = list(data['name'])
   
    try:
        for i in data:
            name = str(i['name']).strip()
            disc = str(i['disc']).strip()
            # price = str(i['price']).replace(',','')
            price = str(i['price']).replace(',','').replace('EGP','').replace('جنيه','')
            im = imgfolder+i['fmg']
            dp = Decimal(price)           
            print(dp,"PRIcE")
            ndp = dp + dp * 10 /100 
            if dp >= 2000 :
                ndp = dp + dp * 5 /100 
            # ndp = dp + dp * 10 /100 
            ndp = Decimal(ndp)
            print(ndp,"nPRIcE")
            ##########
            link = str(i['link']).strip()
            #TODO make sure product not already exist
            if name in ls  :
                ps = Product.objects.filter(name=name,description=disc,outsidelink=link)
                if ps:
                    if(ps.count() > 0):
                        for s in ps :
                            # time.sleep(2)
                            # if name == s.name and ndp == s.price  and disc == s.description and s.outsidelink == link  :
                            if name == s.name  and disc.strip() == s.description.strip() and s.outsidelink.strip() == link.strip() and s.price == dp :
                                print("PRODUCT ALREADY IN DB")         
                            else:
                                print("IT NOT THE SAME ",i['id'])
                                prod = p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)           

                                time.sleep(2)
                                # p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)
            else:
                try:
                    prod = p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)           
                    print("created",i['id'])
                except Exception as ex:
                    print("ERORO WITH",ex)
                # print(newp)
    except  Exception as error:
        # print(newprice,"NP")
        print("ERRROR",error)
    
    return render(request,'add_product.html',{'name':name,'price':price,'im':im})
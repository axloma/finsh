from .models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from cart.cart import Cart
from django.core.paginator import Paginator
import json
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.db.models import Q

def MV_HOLD(request,page,p_I="1"):
    page = page
    #FOR pagination
    p = Paginator(Product.objects.all(),15)#TODO calldb 1perpage
    if page == "CATEGORY":
        category = Category.objects.get(name=p_I)
        #products = Product.objects.filter(Category=category)
        p = Paginator(Product.objects.filter(Category=category),15)
        #products = Product.objects.filter(Category=category)
        #mx = serializers.serialize("json", p,cls=DjangoJSONEncoder)
    elif page == "CATEGORY_M":
        category = Cmenue.objects.get(name=p_I)
        p = Paginator(Product.objects.filter(Category_M=category),15)
        #categorys = Cmenue.objects.filter(Category=category)
        #categorys = ["back",'home']
    pg = request.GET.get('page')
    item= p.get_page(pg)
    item_nums = "a" * item.paginator.num_pages
    products = Product.objects.all()
    # product = Product.objects.get(id=int(p_I))
    first = Product.objects.first()
    firstid = int(first.id)
    # product = Product.objects.get(id=627)
    product = Product.objects.get(id=firstid)


    categorys = Category.objects.all()
    category = Category.objects.get(name="VAPE")
    ids = Cart(request)
    i = list(ids.get_prods2())
    i_dict =  ids.get_prods()
    i.sort()
    # products_s = ()
    quantities = ids.get_quants()
    mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
    if page == "PRODUCT":
        ls = []
        ls.append(p_I)
        pro = Product.objects.filter(id__in=ls)
        product = Product.objects.get(id=int(p_I))
        # images = P_IMG.objects.filter(product=product)
        # product = Product.objects.get(id=int(p_I)).prefetch_related('product_images')

        mx = serializers.serialize("json", pro,cls=DjangoJSONEncoder)
    elif page == "CATEGORY" :
        category = Category.objects.get(name=p_I)

        categorys = Cmenue.objects.filter(Category=category)

        #print("hi")
        #category = Category.objects.get(name=p_I)
        #products = Product.objects.filter(Category=category)
        #p = Paginator(Product.objects.filter(Category=category),5)
        #pg = request.GET.get('page')
        #item= p.get_page(pg)
        #item_nums = "a" * item.paginator.num_pages
        #categorys = Cmenue.objects.filter(Category=category)
        mx = serializers.serialize("json", item,cls=DjangoJSONEncoder)
    elif page == "CATEGORY_M" :
        category = Cmenue.objects.get(name=p_I)
        categorys = Cmenue.objects.filter(name=category)

        #categorys = list(Category.objects.get(name=p_I))
        mx = serializers.serialize("json", item,cls=DjangoJSONEncoder)

    else:
        mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
    dict_M = {'page':page,'mx':mx ,'products':products,'product':product,
              'categorys':categorys,'category':category,'i':i ,'i_dict':i_dict,
              'nums':item_nums, 'quantities':quantities ,'item':item}
    return dict_M



def lives(request):
    products_s = ()
    # if request.POST.get('action') == 'post':
    #get data
    product_str = str(request.POST.get('search'))
    products_n = Product.objects.filter(Q(name__icontains=product_str) | Q(description__icontains=product_str))
    products_s =  list( products_n.values())     
    response = JsonResponse({'product_s':products_s})      
    return response




    


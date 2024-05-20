from .models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from cart.cart import Cart
from django.core.paginator import Paginator
import json
from django.http import JsonResponse,HttpRequest,HttpResponse
from django.db.models import Q

def MV_HOLD(request,page,p_I="1"):
    try:
        page = page
        title = "BSMOKER"
        #FOR pagination
        p = Paginator(Product.objects.all(),15)#TODO calldb 1perpage
        if page == "CATEGORY":
            category = Category.objects.get(name=p_I)
            p = Paginator(Product.objects.filter(Category=category),15)

        elif page == "CATEGORY_M":
            print("REACHCM")
            category = Cmenue.objects.get(name=p_I)
            p = Paginator(Product.objects.filter(Category_M=category),15)

        pg = request.GET.get('page')
        item= p.get_page(pg)
        item_nums = "a" * item.paginator.num_pages
        products = Product.objects.all()
        first = Product.objects.first()
        firstid = int(first.id)
        product = Product.objects.get(id=firstid)
        categorys = Category.objects.all()
        category = Category.objects.get(name="VAPE")
        ids = Cart(request)
        i = list(ids.get_prods2())
        i_dict =  ids.get_prods()
        i.sort()
        quantities = ids.get_quants()
        mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
        if page == "PRODUCT":
            ls = []
            ls.append(p_I)
            pro = Product.objects.filter(id__in=ls)
            product = Product.objects.get(id=int(p_I))
            title = product.name
            mx = serializers.serialize("json", pro,cls=DjangoJSONEncoder)
        elif page == "CATEGORY" :
            category = Category.objects.get(name=p_I)
            categorys = Cmenue.objects.filter(Category=category)
            title = category.name
            mx = serializers.serialize("json", item,cls=DjangoJSONEncoder)
        elif page == "CATEGORY_M" :
            print("CMENU")
            category = Cmenue.objects.get(name=p_I)
            categorys = Cmenue.objects.filter(name=category)
            title = category.name
            #categorys = list(Category.objects.get(name=p_I))
            mx = serializers.serialize("json", item,cls=DjangoJSONEncoder)

        else:
            mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
        dict_M = {'page':page,'mx':mx ,'products':products,'product':product,
                'categorys':categorys,'category':category,'i':i ,'i_dict':i_dict,
                'nums':item_nums, 'quantities':quantities ,'item':item,'title':title}
        return dict_M
    except Exception as eror:
        print("EROR",eror)


#########for search on keyup
def lives(request,foo='cat',pg='home'):
    products_s = ()
    page = pg
    product_str = str(request.POST.get('search'))
    print("PGGG",pg)
    if page == "CATEGORY_M":
        # print()
        cat = Cmenue.objects.get(name=foo)
        products_n = Product.objects.filter(Q(name__icontains=product_str) | Q(description__icontains=product_str) , Category_M=cat)[:15]
    # if request.POST.get('action') == 'post':
    #get data
    elif page == "CATEGORY":
        cat = Category.objects.get(name=foo)   
        products_n = Product.objects.filter(Q(name__icontains=product_str) | Q(description__icontains=product_str) , Category=cat)[:15]
    else:
        products_n = Product.objects.filter(Q(name__icontains=product_str) | Q(description__icontains=product_str) )[:15]
    products_s =  list( products_n.values())     
    response = JsonResponse({'product_s':products_s})      
    return response




    


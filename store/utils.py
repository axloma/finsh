from .models import *
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from cart.cart import Cart
from django.core.paginator import Paginator
def MV_HOLD(request,page,p_I="1"):
    page = page
    #FOR pagination
    p = Paginator(Product.objects.all(),5)#TODO calldb 1perpage
    pg = request.GET.get('page')
    item= p.get_page(pg)
    item_nums = "a" * item.paginator.num_pages
    products = Product.objects.all()
    # product = Product.objects.get(id=int(p_I))
    product = Product.objects.get(id=1)
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
        mx = serializers.serialize("json", pro,cls=DjangoJSONEncoder)
    elif page == "CATEGORY":
        category = Category.objects.get(name=p_I)
        products = Product.objects.filter(Category=category)
        mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
    else:
        mx = serializers.serialize("json", products,cls=DjangoJSONEncoder)
    dict_M = {'page':page,'mx':mx ,'products':products,'product':product,
              'categorys':categorys,'category':category,'i':i ,'i_dict':i_dict,
              'nums':item_nums, 'quantities':quantities ,'item':item}
    return dict_M

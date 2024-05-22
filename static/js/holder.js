################process.js##########

// function getToken(name){
//   var cookieValue = null;
//     if(document.cookie && document.cookie !== ''){
//       var cookies = document.cookie.split(';');
//      for(var i = 0 ; i < cookies.length;i++){
//      var cookie = cookies[i].trim();
//     //does this cookie string begin with the name we want 
//         if(cookie.substring(0,name.length + 1)===( name + '=')){
//           cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
//     break;
//   }} }
//   return cookieValue;
//   }


//window.addEventListener("load", (event) => { }); 
//const csrftoken = Cookies.get('csrftoken');
//console.log("TOKEN",csrftoken)
//var stoken ="{{csrf_token}}"
//console.log("STOKEN",stoken)
/*
//HOLD THIS 
var itemview = document.querySelectorAll('#car_contv');
// var itemc_d = document.querySelector('.c_d');
var itembtnbox = document.querySelector('.btn-box');
itemview.forEach(item => {
  item.addEventListener("click", (e)=>{
    const itemc_p = document.querySelector('.btn-box ');
    const itemc_d = document.querySelector('.menuev ');
    // itemc_p.classList.toggle('open');
    // itemc_d.classList.toggle('open');
      //e.preventDefault()
      console.log(itemc_p)
      console.log(itemc_d)
      console.log("item CLi")
     // $("#mnlist_I").addClass("active");
    //   item.classList.remove("active");
      // xna.classList.add("active");
  });
});
// itemview.addEventListener("onclick", function() {
//   // event.preventDefault();
//   console.log("HI over");
//   itemc_d.classList.toggle("open");
//   itembtnbox.classList.toggle("open");

// });


const rightss = $("#car_contv");  
rightss.click( ()=> {    
    console.log("right clicked");
    // card_rotation.toggleClass("active");
    // setTimeout(alerttime,500);  
    //     
});
// $("#menuicon").toggleClass("open");
*/




// ########### hold for addp
/*
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
    print(allp.count(),"NUMP")
    ls =  []
    ct = "VAPE"
    cm = "disposable"


    for i in allp:
        ls.append(i.name)
    # print(ls)
    # with open('coil.json','r') as file:            
    # with open('elclandispos.json','r') as file: 
    # with open('elclanpod.json','r') as file:
    # with open('media/images_folder/kit/elclankit.json','r') as file:     
    # with open('media/images_folder/coil/elclancoil.json','r') as file:
    # with open('media/images_folder/mod/elclanmod.json','r') as file:
    # with open('media/images_folder/tank/elclantank.json','r') as file:
    # with open('media/images_folder/tools/elclantools.json','r') as file: 
    # with open('media/images_folder/siomarlall/siomarlall.json','r') as file:     
    with open('ovsegdispos.json','r') as file:   
        
            data = json.load(file)
            #print(len(data['name']))
            #name = list(data['name'])
    try:
        for i in data :
            name = i['name']
            price = str(i['price']).replace(',','')
            #FOR ELCLAN dispos
            # newprice = str(i['newprice']).replace(',','').replace('جنيه','')
            # newprice = str(i['newprice']).replace(',','').replace('EGP.','').replace('EGP','')
            # newprice = str(i['newprice'])
            # match = re.search(r'^(.+)\ ?(\.+)$',str(newprice))
            # print(match,"M")
            # if match:
            #     print(match,"x")
            #     newprice = match.group(1)
            # print(newprice)
            # newprice.replace(' .','')
            # disc = str(i['disc'])
            # img = 'images_folder/'+i['img_path']
            # img = 'images_folder/'+i['img_path']
            # img = 'images_folder/kit/'+i['img_path']
            # img = 'images_folder/coil/'+i['img_path']
            # img = 'images_folder/DISPO/'+i['img_path']
            # img = 'images_folder/siomarlall/'+i['fimg']
            my_string = " "
            try:
                Nic = str(i['Nic'])
                Nicl =i['Nico']
                # print(Nicl,'NICL')
                # my_string = ",".join(str(elementx) for elementx in i['Nico'])
                # nl = list(Nicl)
                # string_list = [str(dd) for dd in nl]
                # nlt = []
                
                for x  in Nicl:
                    print(x,"XX")
                    my_string = ",".join(str(cc) for cc in x)
                    print(my_string)
                    # for ix in x:
                    #     nlt.append(ix)
                    #     print(ix,"IT")
                        
                # print(nlt,"ft")
                print("hi")
                # nlt = []
                # for item in nlt:
                    # print(item,"IT")
                # print(string_list)
                # print(Nic)
            except:
                Nic = ""
                Nicl = ""
                print('reach e')
                print(Nicl,'NICL')

            try:
                # Nic = str(i['Nic'])
                simg = 'images_folder/siomarlall/'+i['simg']
                print(simg,"SMG")
                print(Nic)
            except:
                simg = ""
                print(simg,"SMGE")
            # if  i['Nic'] is not None :
            #     print("HI")
           

            ##########
            link = str(i['link'])
            im = 'images_folder/'+i['images'][0]['path']
            # print(im,"IM")
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
            disc = name 
            price2 = price
            price2 = price2[:8]
            dp = Decimal(price2)
            print(dp,"PRIcE")
            # print(price2,"PRICE2")
            # d_price = float(price2)
            if name in ls  :
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
                            if name == s.name and Decimal(dp) == s.price and disc == s.description and s.outsidelink == link:
                                print("PRODUCT ALREADY IN DB IDIOT")
      
                else:
                    print("IT NOT THE SAME ")
                    liquid = Category.objects.get(name=ct)
                    cmenu = Cmenue.objects.get(name=cm)
                    p.objects.create(name=name,price=dp,image=im,description=name,Category=liquid,outsidelink=link,Category_M=cmenu)

                    # p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu,Nic=Nic)           
                    # p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)   
                    # p.objects.create(name=name,price=newprice,image=img,image2=simg,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu,Nic=my_string)   
          
            else:
             
                
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
         

                liquid = Category.objects.get(name=ct)
                cmenu = Cmenue.objects.get(name=cm)
                # p.objects.create(name=name,price=newprice,image=img,image2=simg,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu,Nic=my_string)   

                # p.objects.create(name=name,price=newprice,image=img,image2=simg,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)   

                # p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)             

              
                # p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu,Nic=Nicl)
            
                
                # p.objects.create(name=name,price=newprice,image=img,description=disc,Category=liquid,outsidelink=link,Category_M=cmenu)

                # cmenu = Cmenue.objects.get(name="kit")
                # liquid = Category.objects.get(name="liquid")
                # p.objects.create(name=name,price=dp,image=im,description=ndisc,Category=liquid,outsidelink=link,Category_M=cmenu)
                # p.objects.create(name=name,price=dp,image=im,description=name,Category=liquid,outsidelink=link,Category_M=cmenu)
                p.objects.create(name=name,price=dp,image=im,description=name,Category=liquid,outsidelink=link,Category_M=cmenu)
                # p.objects.create(name=name,price=newp,image=im,description=name,Category=liquid,outsidelink=link)
                # p.objects.create(name=name,price=newp,image=im,description=name,Category=liquid)
                # p.save()
                print("created")

                # print(newp)
    except  Exception as error:
        # print(newprice,"NP")
        print("ERRROR",error)
    
    return render(request,'add_product.html',{'name':name,'price':price,'im':im})




    #########hold registeration form 
    
{% extends "base.html" %}
{% block content  %}


<section class="register yasser_login" >

    <fieldset class="register">
<form action="{% url 'register'  %}" method="POST" >
    {% csrf_token %}
    {%for msg in messages %}
        <h2>{{msg}}</h2>
    {%endfor%}
    <!-- {% if form.errors %}

     <li>   {{ form.errors }} </li>
  
    {% endif %} -->
    {% comment %}
    <!-- {{ form.non_field_errors }} -->
    {{ form.subject.errors }}
    {% endcomment %}
    <small class="btn btn-2 ">{{  form.subject.label_tag  }}</small>

    {% for field in form %}
    {{ form.non_field_errors }}
    <!-- add class to field -->
    {% if field.errors %}

    <li>{{ field.label }}:  {{ field.errors|striptags }}</li>
  {%comment%}  {{ field|add_classes:'active'}} {%endcomment%}
    {% if field.help_text %}
        <small class="btn btn-2  active">{{ field.errors|striptags }}</small>
    {% endif %}

    {% endif %}
    {% endfor %}
    {% for field in form %}
    {% if field.errors %}
    <p class="btn btn-2">{{ field.label }}:
        <small style="color:rgb(245, 15, 7)" class="btn btn-2 active">{{ field.errors|safe }}</small>
 
    </p>
        <{{ field.help_text|cut:"<"|cut:">" }} class="btn btn-2 active">
    {% endif %}
{% endfor %}
    
    <legend>register </legend>
    {{form.as_p}}


    <!--  -->
    {% comment %} <p>
        <label for="username" >username</label>
        <input type="text" name="username" id="username" placeholder="username" autofocus>
    </p> 
    <p>
        <label for="email" >email</label>
        <input type="text" name="email" id="username" placeholder="username" autofocus>
    </p>
    <p>
    <label for="phone" >phone</label>
    <input type="text" name="phone" id="phone" placeholder="username" autofocus>
    </p>
    <p>
    <label for="pass" >password</label>
    <button id="view" onclick="changattr()" class= "btn btn-1 "> view password </button>
    <input type="password" name="pass1" id="pass1" placeholder="password">
    </p>
    <p>
        <label for="pass" >repeat password</label>
        <input type="password" name="pass" id="pass" placeholder="password">
        </p> {% endcomment %}
    <input type="submit" name="login" value="submit"  class="btn btn-1">
    </form>
    
    </fieldset>
    <style>
        ul {
    list-style: none;
    background: gray;
    text-align: start;
    justify-content: flex-start;
}
    </style>
</section>
<script>
var page = "REGISTER";
    let s = document.querySelector(".search");
    {% comment %} s.innerHTML = ""; {% endcomment %}
    //hide cart 
    $("#hs").html("") ;
    $("#cart_n").hide();
    //hide movie 
    $(".movie").html("");
    $(".movie").hide();


</script>

{% endblock  %}


        <!-- {% if field|input_type == 'TextInput' %} -->
        {{ form.name['class'] ="class="btn btn-1 btn-2" }}
        </div>
        <div class="form-group">
        {{ form.email.label(class="btn btn-1 btn-2 ") }}
        {{ form.email(class="btn btn-1 btn-2 active") }}</div>



        {{field.name}}
   {{field.id}}
   {%comment%}
    {{field.help_text}}
    <!-- <p class="btn  "> a</p> -->
    {{field.name}}
    {{field}}
    <!-- <p>{{field}}</p> -->
    {% endcomment %}








    {% if field.errors %}
    {{field.id}}
    <p class="btn btn-2">{{ field.label }}:
        <small style="color:rgb(245, 15, 7)" class="btn btn-1 btn-2 active">{{ field.errors|safe }}</small>
    </p>
    <script>
        var xname = '{{field.name}}'
        console.log("XNAME",xname)
        xl = document.getElementsByName(xname)
        xl.forEach(element => {
            element.classList.add("active");
        
        }); 
     
    </script>
    {% endif %}
{% endfor %}


    {{ form.non_field_errors }}


class CustomModelAdmin(admin.ModelAdmin):  
    list_display = ('get_products')
    def get_products(self, obj):
        return "\n".join([p.name for p in obj.Product.all()])
    
    def __init__(self, model, admin_site):
        self.search_fields = ['id']
        self.list_display = [field.name for field in model._meta.concrete_fields]
        # self.list_display = ([ field.name for field in  model._meta.concrete_fields if not field.many_to_many and not field.one_to_many ])
        # self.list_display = [self.get_products,]

        super(CustomModelAdmin, self).__init__(model, admin_site)



        `
    {% for product in searched %}
<div class="card">
  <div class="car_cont">    
    <img src="{{product.imageURL}}" alt="">
    <h2 class="c_h">'$'{{product.price}}EG</h3>
    <p class="c_d">{{product.description}}</p>    
    <div class="btn-box">
    <select class="btn select" id="select{{product.id}}" >
          {% for key,value in quantities.items %}
          {% if key == product.id|slugify %}
              <option selected >{{value}}</option>
          {% endif %}{% endfor %}
            <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>         
          </select>
      <button type="button" value="{{product.id}}"  id="add-cart"  class="btn btn-1 btn-2 rotation update-cart" data-action='add' data-product={{product.id}}>add to cart </button>  
      <a href="{% url 'product' product.id %}" class="btn btn-2 btn-1 active">view</a>
    </div>
  </div>
</div>
{% endfor %}
`


    `{% for product in res %}
    console.log(product.price,"PRICE");
    <div class="card">
      <div class="car_cont">    
        <img src="{{product.imageURL}}" alt="">
        <h2 class="c_h">'$'{{product.price}}EG</h3>
        <p class="c_d">{{product.description}}</p>    
      
      </div>
    </div>
    {% endfor %}
    `


    //   function s()
//   {
   
//     s_search.addEventListener('click',(e)=> {
//     e.preventDefault()
//     searchfor = search.val().trim();
//     console.log(sf.value,"VALUE");
//     xv = sf.value;
//     // form.submit()
//     return xv;
//   })

// };
//   var searchfor = s()
var eventl = window.MutationObserver || window.WebKitMutationObserver;
evchange = 'DOMSubtreeModified' || "DOMContentLoaded"









//////////////////

var quntityof = 1;
var updateBtn = document.getElementsByClassName('update-cart');
var updateBtnI = document.getElementsByClassName('update-carta');
//mutation observe
var targetNode = document.body;
// configuration of the observer
const config = { characterData: true,subtree: true };
// callback function
const callback = function (observer) { 
    console.log('Changes Detected');
    var CHANGE = true;

    };
// Create observer instance
const observer = new MutationObserver(callback);
// pass in the target node and configuration 
var tf = observer.observe(targetNode, config);
console.log(observer,"OB",callback,"CALLBACK")
console.log("loaded succefully");
console.log(tf,"TRFA")

// var eventl = window.MutationObserver || window.WebKitMutationObserver;
// document.addEventListener(eventl ,(event) => {

    // event.preventDefault()//
evchange = 'DOMSubtreeModified' || "DOMContentLoaded"

// document.body.addEventListener("DOMContentLoaded" ,(event) => { 
    // event.preventDefault() 
for(let item = 0 ; item < updateBtn.length;item++){
    updateBtn[item].addEventListener('click',function(){
        var productId = this.dataset.product 
        var action = this.dataset.action
        var qt = $('#select' + productId + ' option:selected').text()
        if(user == 'AnonymousUser'){
            console.log("USER",user,"action",action)

            addCookieItem(productId,action,qt)
        }else{
            console.log('user logged in')
            //updateUserOrder(productId,action,qt)
        }
   
    })
}
//to update item
for(let x = 0 ; x < updateBtnI.length;x++){
    updateBtnI[x].addEventListener('click',function(){
        console.log("CLICKED UPDATE")
        var producId = this.dataset.index 
        var act = this.dataset.action
        var qt = $('#select' + producId + ' option:selected').text()
        if(page == "cart_summary"  && window.innerWidth > 700 ){
            console.log("window")
            qt = $('#selectx' + producId + ' option:selected').text();
  
          }else{
            qt =  $('#select' + producId + ' option:selected').text();
  
          }
        if(user === 'AnonymousUser'){
            console.log('productId:',producId,'act:',act)
            console.log('Userx:',user)

            addCookieItem(producId,act,qt)
        }else{
            console.log('user logged in')
            //updateUserOrder(productId,act,qt)
        }
   
    })
}

function addCookieItem(productId,action,qt){
    console.log('not logged in ')
    if(action == 'add'){
      if(cart[productId] == undefined){
        if(!qt){
            cart[productId] = 1;
        }else{
        // cart[productId]= {'quantity':1}
         cart[productId] = parseInt(qt);
         //cart[productId] = quntityof;
         //cart[productId] = $('#select' + productId + ' option:selected').text()
        }
        }else{
        //  cart[productId]['quantity'] += 1
        cart[productId] += 1
    }

    }
    if(action == 'remove'){
        console.log("USER",user,"action",action)

        // cart[productId]['quantity'] -=1
        cart[productId] = qt - 1 ;
        // cart[productId] -= 1
        // if(cart[productId]['quantity']<= 0){
           if(cart[productId] <= 0){
            console.log('removed item')
            delete cart[productId]
        }
    }
    if(action == 'update'){
        //var qt = $('#select' + productId + ' option:selected').text()
        console.log("USER",user,"action",action)
        if(!qt || cart[productId] == undefined || qt == "None"){
            console.log('qt none yasser');
            cart[productId] = 1;
        }else{ 
        // cart[productId]= {'quantity':1}
         cart[productId] = parseInt(qt);
         }
    }
    // document.cookie = 'cart='+JSON.stringify(cart)+"; path=/";
    document.cookie = 'cart='+JSON.stringify(cart)+";domain; path=/";
}

    //send dat to backend with ajax

function updateUserOrder(productId,action,qt){
    console.log('user logged in')
   
    var url = '/update_item/'
    fetch(url,{
        method: 'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,
        },
        body:JSON.stringify({"productId":productId,"qt":qt,"action":action})
    })
    .then((response)=>{
        return response.json()
    })
    .then((data) => {
        //clear cart by reassign it 
        cart = {}
        document.cookie = 'cart='+JSON.stringify(cart)+";domain; path=/";     
    })
}

// });



  {% comment %} <script  src="{% static 'js/mainjs.js' %}"></script> {% endcomment %}
  {% comment %} <script src="{% static 'js/nav.js' %}"></script> {% endcomment %}
<!-- <script type="text/javascript" src="{% static 'js/nav.js' %}" ></script> -->
<!-- <script  type="text/javascript" src="{% static 'js/nav.js' %}" ></script> -->

{% extends "base.html" %}  
{% load static %}

{%block content %}      
<section class="home" id="try">
  {% comment%}
<!-- {% for product in products %} -->
{% endcomment %}

{% for product in searched %}
<div class="card">
  <div class="car_cont">    
    <img src="{{product.imageURL}}" alt="">
    <h2 class="c_h">${{product.price}}EG</h3>
    <p class="c_d">{{product.description}}</p>
     
    <div class="btn-box">
    <select class="btn select" id="select{{product.id}}" >
          <!-- {% for key,value in quantities.items %}
          {% if key == product.id|slugify %} -->
              <option selected >{{value}}</option>
          {% endif %}{% endfor %}
            <option value="1">1</option>
          <option value="2">2</option>
          <option value="3">3</option>
          <option value="4">4</option>
          <option value="5">5</option>
          
          </select>
      <button type="button" value="{{product.id}}"  id="add-cart"  class="btn btn-1 btn-2 rotation update-cart" data-action='add' data-product={{product.id}}>add to cart </button>  
      <a href="{% url 'product' product.id %}" class="btn btn-2 btn-1 active">view</a>
    </div>
  </div>
</div>
{% endfor %}
<!-- <form action="" class="" method='GET'> -->
<!-- <button type="button" id="load"  class="btn btn-1 btn-2"  center>more</button>   -->

<!-- </form> -->
</section>
<button type="submit" name="" id="load"  class="btn btn-2 ">LOAD MORE</button>

<script >
///////////////////////////////////////////////////////////////

    // var d = document.querySelectorAll(".rotation");
    let carts = document.getElementById('cart_n');
    let in_cart_a = {{ i|safe }};
    //var cart = JSON.parse(getCookie('cart'))
    console.log(in_cart_a.length,"inL")
    var urlx = "{% url 'cart_add' %}"
    var urld = "{% url 'cart_delete' %}"
    var c_ur = "{% url 'category' '*' %}"

    console.log(urlx)
    var page = "{{page}}";
    console.log(page,"PAGE")
    



</script>

{%block javascript}
<script>
  const s_search = document.getElementById('s_search')
  const form = document.getElementById("sform")
  let sf = document.getElementById("search")
  var xv = "{{serchfor}}"
  let limit = 15
  let vi = document.getElementById("try")
  htmlx = ""


document.getElementById('load').addEventListener('click',()=>{
console.log("BTNCLICK")
console.log("LIMIT",limit+=6)
loadmore()
limit+=6

})

  function loadmore(){
$.ajax({
  type:'GET',
  url : `/search/${limit}`,
  data: {sfor:xv},
  success:function(response){
    console.log("SUCESS");
    // console.log(response['mx'])
    console.log(response.data);
    console.log(response.mxl,"END");
    const res = response.data;
    if ( response.mxl){
      $("#load").addClass('active').attr('disabled','disabled').text("END")
        console.log(limit,"L",response.mxl,"MXL")
    };
      // console.log(product,"PROD")
   
    // res.forEach((value)=> {
    $.each(response.data, function(key, pvalue) {
      // console.log(element.name,"NAME");
      htmlx +=`<div class="card" id="card" value={{data}}>
              <div class="car_cont">    
                <img src='/media/${pvalue.image}' alt="">
                <h2 class="c_h">$${pvalue.price}EG</h3>
                <p class="c_d">${pvalue.description}</p>
                <div class="btn-box">
                  <select class="btn select" id="select${pvalue.id}" >
                    <option selected >1</option>  
                </select>
                <button type="button" value=${pvalue.id}  id="add-cart"  class="btn btn-1 btn-2 rotation update-cart" data-action='add' data-product=${pvalue.id}>add to cart </button>  
                <a href='/product/${pvalue.id}' class="btn btn-2 btn-1 active  id="viewel">view</a>
              
                </div>
          </div>
        </div>`                   
        
    });

    // pageelement = $("#try").html() 
    // console.log("HTMLX",htmlx)
    // pageelement += htmlx
    // console.log(pageelement)
  
    // vi.texetContent += htmlx ;
    // $("#try").html(htmlx)
    // vi.innerHTML += htmlx ;
    vi.insertAdjacentHTML('beforeend',htmlx);
    // let opt = document.createElement('section');     
    // opt.innerHTML =htmlx;
    // vi.appendChild(opt)
    // $("#try").html(pageelement)
//  htmlx
  // var closeButton = document.createElement ('section');
  // closeButton.className = 'home';
  // closeButton.innerHTML = htmlx;
  },
  error:function(error){
    console.log(error)
  }

})}

  
  // console.log(searchfor,"SEARCHFOR")
  // test('DOMSubtreeModified');
  //       test('DOMNodeInserted');
  //       test('DOMNodeRemoved');
  // evchange = 'DOMSubtreeModified' || 'DOMNodeInserted' || 'DOMNodeRemoved'
  // window.addEventListener('DOMSubtreeModified',()=>{
  //   console.log("MODIFIED")

  // })  
</script>

{%endblock javascript}
<script type="text/javascript" src="{% static 'js/nav.js' %}" ></script>
{%endblock%}





/*
    ///////hide and show
    var update = document.getElementsByClassName('card');
    // const itemc_p = document.querySelectorAll('.menuev ');
    const itemc_p = document.querySelectorAll('.btn-box  ');
    const itemc_d = document.querySelectorAll('.c_d ');
    for(let item = 0 ; item < update.length;item++){
    update[item].addEventListener('click',function(){    
      itemc_p[item -1].classList.toggle('open')
      itemc_d[item ].classList.toggle('open')
      // itemc_p.classList.toggle('open');
      // $(".c_d").toggleClass("open");
      console.log("HIHI")
    })
}

var update = document.querySelectorAll('#car_contv');
    // const itemc_p = document.querySelectorAll('.menuev ');
    
    for(let item = 0 ; item < update.length;item++){
    const itemc_p = document.querySelectorAll('.btn-box  ');
    const itemc_d = document.querySelectorAll('.c_d ');
    update[item].addEventListener('click',function(){    

      itemc_p[item ].classList.toggle('open')
      itemc_d[item + 1 ].classList.toggle('open')
      // itemc_p.classList.toggle('open');
      // $(".c_d").toggleClass("open");
      console.log("HIHI")
    })
}
*/
/*
var update = document.querySelectorAll('#car_contv');
    // const itemc_p = document.querySelectorAll('.menuev ');
    
    for(let item = 0 ; item < update.length;item++){
    const itemc_p = document.querySelectorAll('.btn-box  ');
    const itemc_d = document.querySelectorAll('#c_dmv');
    update[item].addEventListener('click',function(){    

      itemc_p[item ].classList.toggle('open')
      itemc_d[item ].classList.toggle('open')
      // itemc_p.classList.toggle('open');
      // $(".c_d").toggleClass("open");
      console.log("HIHI")
    })
}

*/


                //<button type="button" value=${pvalue.id}  id="add-cart"  class="btn btn-1 btn-2 rotation update-cart" data-action='add' data-product=${pvalue.id}>add to cart </button>  



//add product with single img in same folder 
/*
def add_p(request):
    #insert from scrapy 
    p = Product 
    allp = Product.objects.all()
    print(allp.count(),"NUMP")
    ls =  []
    ct = "SMOKING"
    cm = "melliferous-معسل"
    cat = Category.objects.get(name=ct)
    cmenu = Cmenue.objects.get(name=cm,Category=cat)
    jsonfile = "media/images_folder/mo3ez/mo3ez.json"
               #media/images_folder/amazonaccess/amazonacess.json
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    # imgfolder = '/images_folder/mo3ez/proi/'
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    imgfolder = '/images_folder/mo3ez/'

    for i in allp:
        ls.append(i.name)
    # print(ls)
    listimg = []
    with open(jsonfile,'r') as file:           
            data = json.load(file)
            #print(len(data['name']))
            #name = list(data['name'])
    # with open(imgf,'r') as imgfile:
    #         imgdata = json.load(imgfile)
    #         for i in imgdata:
    #             dicimg = {}
    #             dicimg['link'] = i['link']
    #             dicimg['images'] = i['images']
    #             # time.sleep(5)
    #             print("IMGAGES",dicimg['images'])
    #             listimg.append(dicimg)
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
            # proimages = []
            ##########
            link = str(i['link']).strip()
            # for l in listimg :
            #     if link == l['link']:
            #         proimages = l['images'] 
            #         print(link,"LINK",proimages,"IMGAGES")
            # im = imgfolder+i['fmg']
            # im = imgfolder+proimages[0]
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
                                # p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)
            else:
                try:
                    prod = p.objects.create(name=name,price=dp,image=im,description=disc,Category=cat,outsidelink=link,Category_M=cmenu)
                    # for img in proimages:
                    #     im = imgfolder+ str(img)
                    #     P_IMG.objects.create(product=prod,image=im)

                    print("created",i['id'])
                    # time.sleep(1)
                except Exception as ex:
                    print("ERORO WITH",ex)
                # print(newp)
    except  Exception as error:
        # print(newprice,"NP")
        print("ERRROR",error)
    
    return render(request,'add_product.html',{'name':name,'price':price,'im':im})



//add product with single img in same folder 
/*
def add_p(request):
    #insert from scrapy 
    p = Product 
    allp = Product.objects.all()
    print(allp.count(),"NUMP")
    ls =  []
    ct = "SMOKING"
    cm = "melliferous-معسل"
    cat = Category.objects.get(name=ct)
    cmenu = Cmenue.objects.get(name=cm,Category=cat)
    jsonfile = "media/images_folder/mo3ez/mo3ez.json"
               #media/images_folder/amazonaccess/amazonacess.json
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    # imgfolder = '/images_folder/mo3ez/proi/'
    # imgf = 'media/images_folder/mo3ez/proi/product_img.json'   
    imgfolder = '/images_folder/mo3ez/'

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
                            if name == s.name  and disc.strip() == s.description.strip() and s.outsidelink.strip() == link.strip()  :         
                            else:
                                print("IT NOT THE SAME ",i['id'])
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
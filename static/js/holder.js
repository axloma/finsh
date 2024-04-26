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


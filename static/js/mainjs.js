
var quntityof = 1;
var updateBtn = document.getElementsByClassName('update-cart');
var updateBtnI = document.getElementsByClassName('update-carta');
console.log("loaded succefully");


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


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
var csrftoken = getToken('csrftoken');
document.addEventListener("DOMContentLoaded", (event) => {
 



//window.addEventListener("load", (event) => { }); 
//const csrftoken = Cookies.get('csrftoken');

//console.log("TOKEN",csrftoken)
//var stoken ="{{csrf_token}}"
//console.log("STOKEN",stoken)
    
      if( in_cart_a.length > 0){
        $('#cart_n_a').addClass(" active");
        $("#cart_n").show();

                                }         
                                    
//check if item exist in cart already
    d.forEach(link => {
      var pq = $('#select' + link.value + ' option:selected').text();
      // var pq = $('#select' + link.value ).val();

      if(!pq || pq == undefined || pq == "None"){
        console.log('pq none yasser',pq);
        pq = "1";
      }
      event.preventDefault();
      //with js loop and get 
      for(i=0 ; i < in_cart_a.length ; i++){
        if ( link.value == in_cart_a[i] ){
        link.classList.remove("rotation");
        link.textContent = " remove from cart  ";
        link.dataset.action = "remove";
        }
    }
//
    link.addEventListener("click", (e)=>{
      //e.preventDefault();
////////TODO add item if it doesn't exist
     pq = $('#select' + link.value + ' option:selected').text();

      if(in_cart_a.includes(link.value) == false){	

        $.ajax({
          type:'POST',
          url: urlx,
          data:{
          product_id: link.value,
          // product_qty: "1",
          product_qty: pq ,
          csrfmiddlewaretoken: csrftoken,
          action: 'post'
        },                         
        success:function(js){                                                               
          // carts.setAttribute('data-content', json.qty); 
          console.log(in_cart_a.length,"LN2")
          in_cart_a.push(link.value);
          link.classList.toggle("rotation");
          link.textContent = " in cart ";
          link.dataset.action = "remove";
          $('#cart_n_a').addClass("active");
          $("#cart_n").show();
          console.log(in_cart_a.length,"inL2")
          carts.setAttribute('data-content', in_cart_a.length)
          carts.setAttribute('data-content',js.qty)
          console.log("sucess from outside",js.qty)
          if  (js.qty == undefined ){
               console.log("SOMETHING WRONG ")
              }
          console.log(js,"JSON")
    },
        error: function(xhr,errmsg,err){
        console.log("error adding",errmsg,err,xhr);
        }
    });

///////remove item if it does exist 
    }else if ( in_cart_a.includes(link.value) == true){
      // pq = $('#select' + link.value + ' option:selected').text();

      $.ajax({
      url: urld,
      type:'POST',
      data:{
      product_id: link.value,
      product_qty: pq,
     // product_qty: "1",
      csrfmiddlewaretoken: csrftoken,
      action: 'post'
      },       
        success:function(json){                                                      
          carts.setAttribute('data-content', json.qty);
          //$('#select'+link.value).text(json.pq).change();
          $('#select'+link.value).val(json.pq).change();
          //check for item quantity while remove it 
          if(json.pq <= 0 || json.pq == "NaN" || json.pq == "None" || json.pq == "NoNE" || json.pq == "null") {
            in_cart_a.splice(in_cart_a.indexOf(link.value),1);  
            link.classList.toggle("rotation");
            link.textContent = "add m to cart ";
            link.dataset.action = "add";
            location.reload()

          }
        },
        error: function(xhr,errmsg,err){
          console.log(" error deleteing");
      }
      });
          
      }   });  });  
//update item quantity on click
      $(document).on('click','.update-carta',function(e){
        e.preventDefault(); 
        var productid = $(this).data('index');
        $.ajax({
            type:'POST',
            url: urlu,
            data: {
                product_id: $(this).data('index'),
                product_qty: $('#select' + productid + ' option:selected').text(),
                csrfmiddlewaretoken:csrftoken,
                action:'post'        
            },
            success: function(json){
                console.log("success update cart dic");
               // location.reload();//TODO reload afer update
            },
            error:function(xhr,errmsg,err){
                console.log("error");
            }
        });
    });
  });
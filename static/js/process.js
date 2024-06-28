var csrftoken = getToken('csrftoken');
var update = document.querySelectorAll('#car_contv');

document.addEventListener("DOMContentLoaded", (event) => {
  var d = document.querySelectorAll(".rotation");

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
      e.preventDefault();
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
          //total = json.total
          //$('#total').text('TOTAL PRICE:$'+js.total).change();
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
          $('#selectx'+link.value).val(json.pq).change();
          total = json.total
          $('#total').text('TOTAL PRICE:$'+json.total).change();
          //check for item quantity while remove it 
          if(json.pq <= 0 || json.pq == "NaN" || json.pq == "None" || json.pq == "NoNE" || json.pq == "null") {
            in_cart_a.splice(in_cart_a.indexOf(link.value),1);  
            link.classList.toggle("rotation");
            link.textContent = "add to cart ";
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
        var prq =  $('#select' + productid + ' option:selected').text();
         // product_qty: $('#select' + productid + ' option:selected').text(),
        if(page == "cart_summary"  && window.innerWidth > 700 ){
          console.log("window")
          prq = $('#selectx' + productid + ' option:selected').text();

        }
        else {
          prq =  $('#select' + productid + ' option:selected').text();

        }    
        $.ajax({
            type:'POST',
            url: urlu,
            data: {
                product_id: $(this).data('index'),
                product_qty: prq,
                csrfmiddlewaretoken:csrftoken,
                action:'post'        
            },
            success: function(json){
                console.log("success update cart dic");
                $('#select'+productid).val(json.qty).change();
                $('#selectx'+productid).val(json.qty).change();
                $('#total').text('TOTAL PRICE:$'+json.total).change();
                total = json.total
                console.log(json.total,"TOTAL");
               // location.reload();//TODO reload afer update
            },
            error:function(xhr,errmsg,err){
                console.log("error");
            }
        });
    });
  });


  // const itemc_p = document.querySelectorAll('.menuev ');
 
  //TODO show button box of each card 
    const itemc_p = document.querySelectorAll('.btn-box  ');
  const itemc_d = document.querySelectorAll('#c_dmv');
  for(let item = 0 ; item < update.length ;item++){

  update[item].addEventListener('click',function(e){    
    console.log(this.nodeName,"NAME")
    const t = e.target
    const fchild = this.children[0].children[5];
    const schild = this.children[0].children[3];
    console.log(fchild.nodeName,"NODENAMECHILD")
    fchild.classList.toggle('open')
    schild.classList.toggle('open')
    // itemc_p[item ].classList.toggle('open')
    // itemc_d[item ].classList.toggle('open')
    // itemc_p.classList.toggle('open');
    // $(".c_d").toggleClass("open");
    console.log("HIHI",fchild.nodeName)
  })
}
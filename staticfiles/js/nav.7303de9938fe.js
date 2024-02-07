
   
    var size = window.innerWidth ;
    var section = document.getElementById('cart_sec');
    window.addEventListener("load", (event) => {
      event.preventDefault();
      //$("#hs").html("") ;
      $("#hs").hide();
      $("#cart_n").hide();
      if(page == "CATEGORY"){
        $("#hs").show();
        $("#all").removeClass("active");
      }
      $("#mnlist_I").click(()=> {
        $("#all").removeClass("active");
        $("#mnlist_I").addClass("active");
      });
      console.log("PAGE",page)
      if( size <= 700){
          section.classList.remove("product_view");

      }
      if( in_cart_a.length > 0){
        console.log("item  in card");
        $('#cart_n_a').addClass("btn btn-1 active");
        console.log(in_cart_a.length + "l");
        $("#cart_n").show();
        if(page == "CART"){
            $("#cart_n").hide();
        }
    } 
      console.log("size",size);
  });
  window.addEventListener("resize",(event)=>{
      console.log("size",window.innerWidth);
      if( window.innerWidth <= 700){
          section.classList.remove("product_view");

      }else{
          section.classList.add("product_view");
      }
  }); 
  if(page == "CATEGORY"){
    $("#hs").show();
  }
  
//   var m = document.querySelectorAll(".LTEST");
//   m.forEach( item => {
//       item.addEventListener("click", (e)=>{
//           //e.preventDefault()
//           console.log(item)
//           console.log("item CLi")

//           item.classList.remove("active");
//       });
//   });
var m = document.querySelectorAll(".LTEST");
  m.forEach( item => {
    const xna = item.firstElementChild;
    // item.classList.remove("active");
      item.addEventListener("click", (e)=>{
          //e.preventDefault()
          console.log(item)
          console.log("item CLi")
         // $("#mnlist_I").addClass("active");
        //   item.classList.remove("active");
          xna.classList.add("active");
      });
  });
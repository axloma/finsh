  var EMPITYF = []
    document.getElementById('form').addEventListener('click',function(e){
        e.preventDefault();
        console.log('form submitted');
        //check for empty field 
        console.log(inp.length)
         //inp.forEach( link => {
    //const xna = item.firstElementChild;
      for(let item =0 ; item < inp.length ; item++){
          if (inp[item].value == ""){
            inp[item].classList.add("active");
            console.log(inp[item].name)
            //alert("EMPTY"+inp[item].name)
            EMPITYF.push(inp[item].name)
            //alert("FIELDN",inp[item]);
          }
          else{
            inp[item].classList.remove("active");
          }
      }
       // });
        
        submitFormData();
       
    })
    function submitFormData(){
        console.log('payment btn clic')
        var userFormData = {
            'name':null,
            'email':null,
            'total':total,
            'address':null,
            'city':null,
            'state':null,
            'zipcode':null,
            'phone':null,
        }
        var shipping = '{{order.status}}'
        console.log(shipping)
        userFormData.name = form.name.value
        userFormData.email = form.email.value
        userFormData.address = form.address.value
        userFormData.city = form.city.value
        userFormData.state = form.state.value
        userFormData.zipcode = form.zipcode.value
        userFormData.phone = form.phone.value 
        //var url ='process_order/'
        var url = process
        fetch(url,{           
            method:'POST',
            headers:{
            'Content-Type':'application/json',
            'X-CSRFToken': csrftoken,

            },
            body:JSON.stringify({"form":userFormData})
        })
        .then((response) => response.json())
        .then((data) => {
              console.log(typeof(data))
              console.log(typeof(data.error),data.error)
           // if (data == "error"){
              if(data.error){
                var e = data.error
              if (e == "EMPITY FIELD"){
                console.log(e)
                console.log(typeof(data.error),data.error)

              alert("MISSING FIELD" + EMPITYF)
              EMPITYF = []
              var M = document.getElementById("msgx");
              //show msg from django   
              for ( let i = 0 ; i < data.MSG.length ; i ++){
                $("#msgx").text(data.MSG[i].message).change();
              }

              }else if (e == "EMAIL_E"){
      
               alert("EMAIL NOT VALIED")
              //window.location.href = "{% url 'cart_summary' %}"
              var EM = document.getElementById("EMAIL");
              EM.classList.add("active");        
              for ( let i = 0 ; i < data.MSG.length ; i++){
                $("#msgx").text(data.MSG[i].message).change();
              }
             
              //location.reload();
              }
            }
            else{
          
           alert('transiction completed');
           cart = {}
           document.cookie = 'cart='+JSON.stringify(cart)+";domain; path=/";
           //window.location.href = "{% url 'home' %}"
           window.location.href = home
           //location.reload()
            }
          
        })

          
  }
  

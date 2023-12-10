//get items inside local storge 
var items = {}, ls = window.localStorage;
for (var i = 0, k; i < ls.length; i++)  {
items[k = ls.key(i)] = ls.getItem(k);
return items;
console.log(JSON.stringify(items) ,+"items");
}

//console.log(JSON.stringify(window.localStorage) + "local"); //check local storge










////////////
const card_rotation = $("#card_rotation");
const right = $("#right");
const img_src = $("#img_src");
right.click( ()=> {
    const ride = new Promise((resolve,reject) => {
        console.log("right clicked");
        card_rotation.toggleClass("active");
        //code if sucess
        if('success'){
        resolve('sucess');
        }else{
            reject('failed');
        }
        });
        //
        ride 
        .then( (msg)=> {
        console.log(msg);
        alerttime();
        }).catch((msg)=>{
        console(msg);
        });
        
   
   // let xtime = setTimeout(alerttime,600);
    function alerttime(){
        var img = $("#img_src").attr('value');
        console.log(img);
        img_src.attr('src', img);
        console.log("card_rotate");

                       }
   

});







function todo(callback){
    console.log("right clicked");
    card_rotation.toggleClass("active");
    callback();
}
function tocall() {
    var img = $("#img_src").attr('value');
    console.log(img);
    img_src.attr('src', img);
    console.log("card_rotate");
}
todo(tocall);//TODO without printcess 





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




$('img').on({
    'click': function() {
         var src = ($(this).attr('src') === 'img1_on.jpg')
            ? 'img2_on.jpg'
            : 'img1_on.jpg';
         $(this).attr('src', src);
    }
});
17

I'll show you how to change the image src, so that when you click an image it rotates through all the images that are in your HTML (in your d1 id and c1 class specifically)... whether you have 2 or more images in your HTML.

I'll also show you how to clean up the page after the document is ready, so that only one image is displayed initially.

The full code

$(function() {

    var $images = $("#d1 > .c1 > a").clone();  

    var $length = $images.length;
    var $imgShow = 0;

    $("#d1 > .c1").html( $("#d1 > .c1 > a:first") );  

    $("#d1 > .c1 > a").click(function(event) { 

        $(this).children().attr("src", 
                        $("img", $images).eq(++$imgShow % $length).attr("src") );
        event.preventDefault();

    });
});
Create a copy of the links containing the images (note: you could also make use of the href attribute of the links for added functionality... for example display the working link below each image):

    var $images = $("#d1 > .c1 > a").clone();  ;
Check how many images were in the HTML and create a variable to track which image is being shown:

var $length = $images.length;
var $imgShow = 0;
Modify the document's HTML so that only the first image is being shown. Delete all the other images.

$("#d1 > .c1").html( $("#d1 > .c1 > a:first") ); 
Bind a function to handle when the image link is clicked.

    $("#d1 > .c1 > a").click(function(event) { 
        $(this).children().attr("src", $("img", $images).eq(++$imgShow % $length).attr("src") );
        event.preventDefault();
    });
The heart of the above code is using ++$imgShow % $length to cycle through the jQuery object containing the images. ++$imgShow % $length first increases our counter by one, then it mods that number with how many images there are. This will keep the resultant index cycling from 0 to length-1, which are the indices of the $images object. This means this code will work with 2, 3, 5, 10, or 100 images... cycling through each image in order and restarting at the first image when the last image is reached.

Additionally, .attr() is used to get and set the "src" attribute of the images. To pick elements from among the $images object, I set $images as the jQuery context using the form $(selector, context). Then I use .eq() to pick just the element with the specific index I'm interested in.




//get items inside local storge 
var items = {}, ls = window.localStorage;
for (var i = 0, k; i < ls.length; i++)  {
items[k = ls.key(i)] = ls.getItem(k);
return items;
console.log(JSON.stringify(items) ,+"items");
}

//console.log(JSON.stringify(window.localStorage) + "local"); //check local storge
let data = "asdansdas asd najksd kajsnd ajnd akjd nakjdn kjasd  <h1>alksdaslkdmalks</h1> alskdn aslkda klasd <h1> alkjsdanskjd </h1>";
let re = ""    
let nuevoStr = ""                              
if(data.includes("seo-content")){
    re = /(?<=seo-content\s*)(<h1[^>]*>)([\s\S]*?)(<\/h1>)/;
    nuevoStr = data.replace(re, '$1{target_url.h1}$3');
} else {
    re = /(<\/h1>)([\s\S]*?)(<h1)/g;
    nuevoStr = data.replace(re, '$1<h2>$2{target_url.h1}</h2>$3');
}
console.log(nuevoStr)
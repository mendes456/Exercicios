window.addEventListener('focus', event =>{

    console.log("focus");
});



document.addEventListener('click', event =>{
    console.log("click");

});


let agora = new Date();
console.log(agora.toLocaleDateString("pt-BR"));



let cursos = ["HTML","CSS", "JavaScript", 10, true,new Date(), function(){}];

cursos.forEach(function(value,index){
    console.log(index,value)
});
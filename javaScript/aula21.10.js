let celular =  function(){

        this.cor ="azul";
        
}

let objeto =  new celular();

console.log(objeto);



let telefone=  function(){

    this.cor ="azul";

    this.ligar = function(){
        console.log ("uma ligacão");
        return "ligando"
    }
    
}

let obj =  new telefone();
console.log(obj.ligar());

//outro modo 


let cel = function(){
    this.cor = "azul";

    this.ligar = function(){
        console.log ("uma ligação");
        return "ligando";

    }
}

let objet = new cel();
console.log(objet.ligar());
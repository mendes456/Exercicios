var olaMundo = "Olá mundo!";

console.log(olaMundo);


console.log("olaMundo");
console.log('olaMundo');
console.log(`olaMundo`);


let a=10;
const b= "10";

console.log(a==b);

/* var,let e const são tipos de variaveis */

/*  a=b -> b esta sendo atribuido  */
/*  a==b -> comparando de 4é igual ao b  */
/*  a===b ->  tipos e variaeis são iguais  */



/*[Nome do aluno] tem [idade aluno], peso [peso aluno] tem [altura aluno] de altura e seu IMC é de [imc aluno]*/
// IMC= peso/(altura*altura)


const nome='Alexandre';
const sobrenome= 'Rocha de Souza';
const idade=18;
const peso=100;
const altura=1.80;
let imc= peso/altura**2;
let anoNascimento;


console.log(nome, sobrenome, 'tem', idade, 'anos peso', peso, 'kg');
console.log(altura, 'de altura e seu IMC é de', imc);

console.log(`${nome} ${sobrenome} tem ${idade} anos ${peso} kg`);
console.log(`${altura} de altura e seu IMC é de ${imc}`)


// Alert, Confirm e Prompt     (Prova)

let num1= prompt('Digite um número');
let num2= prompt('Digite outro número');

num1 = Number(num1)
num2 = Number(num2)

const resultado= (num1 + num2);

alert (` O resultado da sua conta foi ${resultado}`);



// Alert, Confirm e Prompt     (Prova)

let numero1= prompt('Digite um número');
let numero2= prompt('Digite outro número');

numero1 = Number(numero1)
numero2 = Number(numero2)

//const resultado= (num1 + num2);

alert (` O resultado da sua conta foi ${numero1+numero2}`);

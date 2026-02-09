const alunos = ['Brenda', 'wallace','wilde']

console.log(alunos);
console.log(alunos[0]);
console.log(alunos[1]);
console.log(alunos[2]);


//aletrando o valor da posição

alunos[2] ='jose';
console.log(alunos);


//exibindo o tamanho do array (lenght)
console.log(alunos.lenght);


//adicionando um elemento ao final da array (push)

alunos.push('bruno');
console.log(alunos);

// adicionando um elemento no ínicio do array = vetor -- (unshift)
alunos.unshift('miguel');
console.log(alunos);


// remove o ultimo elemento do array (pop)
alunos.pop();
console.log(alunos);

//remove o ultimo elemento do array (shift)
alunos.shift();
console.log(alunos);


//deletando elemento de um indice do array (delete)
delete alunos[1];
console.log(alunos);


//fatiando array, o ultimo elemento não é incluso
console.log(alunos.slice(0,2));






//criando objetos

const pessoa  = {
    nome:'alexandre',
    sobrenome: 'rocha',
    idade: 18
};


console.log(pessoa.nome);
console.log(pessoa.sobrenome);
console.log(pessoa.idade);


// cor do sinal (semaforo)

let cor ='verde';

if (cor === 'verde'){
    console.log('siga');
} else if (cor === 'amarelo'){
    console.log('atenção');
} else {
    console.log('pare')
}



//conta de vezes

let n = 5;

for(let i = 0; i <= 10; i++){
    console.log(`${i} X ${n} = ${i*n}`);
}


//soma

function somar(x1,x2){
    return x1 + x2;
}

let resultado = somar(5,8);
console.log(resultado);

//funcao para criar pessoa

function criarPessoa (nome,sobrenome,idade){
    return {nome,sobrenome,idade};
}

 const pessoa1= criarPessoa('Brenda', 'Mendes',26);
 const pessoa2= criarPessoa('Wallace', 'Braga', 27);
 const pessoa3= criarPessoa('Anna', 'Celeste', 24);

 console.log(pessoa1.nome, pessoa1.sobrenome);
 console.log(pessoa2);
 console.log(pessoa3.nome);
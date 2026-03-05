import datetime

Dia_Hoje = datetime.datetime.today().date()
print( f'Hoje e: {Dia_Hoje} \n')

Data = datetime.date(2024, 4, 15)
print(f'Construindo uma Data {Data} \n')

Ano = Data.year
Mes = Data.month
Dia = Data.day
print(f'Hoje e fia {Dia} do mes {Mes} do ano de {Ano} \n')

Intervalo = Data - Dia_Hoje
print(f'Ja ocorreu {Intervalo} dias \n')

Novo_Formato = Dia_Hoje.strftime('%d/%m/%y')
print( f'Hoje e: {Novo_Formato} \n')

print(f'Somando 30 dias,{Dia_Hoje + datetime.timedelta(days = 30)}')
print(f'Diminuindo 30 dias,{Dia_Hoje - datetime.timedelta(days = 30)}')


import random # sortear nmeros aleatorios

Lista_Numerica = [1, 2, 3, 4, 5, 6]
print(f'O numero sorteado foi: {random.choice(Lista_Numerica)} \n')

Palavra = 'Goku'
print(f'A Letra sorteada foi: {random.choice(Palavra)} \n')

Numero_Aleatorio = random.random()
print(f'O Numero gerado foi: {Numero_Aleatorio} \n')

Numero_Aleatorio_01 = random.randint(0, 10)
print(f'O Numero aleatorio entre 1 e 10 foi: {Numero_Aleatorio_01} ')


Idade = 20

if Idade >= 18:
    print('Voce e maior de idade!')



Idade = int(15)

if Idade >= 18:
    print('Voce e de maior')

else:
    print('Voce e menor de Idade')
    

# for = para (repeticão determinada )
    
    
for numero in range(10):
    print(numero ** 2)
    

Lista_Paises = ['Brasil', 'Argentina', 'Uruguai', 'Chile', 'Paraguai', 'Bolivia', 'Equador', 'Colombia', 'Suriname', 'Goianai France']
for Loop in Lista_Paises: 
    print(Loop)
    
Loop = 0


# while= enquanto (repetição indeterminada)

while Loop <= 10:
    print(Loop)
    Loop += 1
    


#funcão simples
    
def Somar(Valor1, Valor2):
    Soma = Valor1 + Valor2
    print(Soma)
    
Somar(10, 20)


#estrutura de classe/classes

class Pessoa:
    
    #método construtor
    def __init__(self, Nome, Idade):
        self.Nome = Nome
        self.Idade= Idade
        
    def Boas_Vinda(self):




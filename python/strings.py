
#Strings (fatiamentos)

Minha_string= 'me de a sua força, pégasus!'
print(type(Minha_string)) #type é o tipo de dados da variavel
print(len(Minha_string)) #total de caracter na frase

print(Minha_string[0]) # conta de 0,1,2,3,4,5
print(Minha_string[5])
print(Minha_string[-1]) # quando tiver o sinal de menos conta de tras pra frente
print(Minha_string[-10])
print(Minha_string[0:10]) #até (conta até 10 e vai contar ate o 9)

print('\n')
print('\n')

#-----------------------------------------------------------------------------------------------------------------------------------

#imprimindo uma string

teste=('quem é esse')

print(teste)
print('\n')

#tipo de uma strihng
print(type(teste))
print('\n')

#tamanho de uma string
print(len(teste))
print('\n')

#concatenacao
print(teste + ' pokemon?')
print('\n')

#substitui uma substring por qualquer outra coisa

substituir = teste.replace('quem é esse', 'acredite no coracao das cartas')
print(substituir)


#------------------------------------------------------------------------------------------------------------------------------

azul= str('a Brenda é muito linda')

#a teste s começa com "Olá"?
print(azul.startswith('Olá'))

#a teste termina com "mundo"?
print(azul.endswith('mundo'))

#quantas ocorrencias da palavra "m" a string possui?
print(azul.count('m'))

#capitalize - transformar a primeira letra da primeira palavra em maiuscula.
azul_02="goku"
print(*azul_02.capitalize())

#verificar se uma string só possui números
azul_03='123456789'
azul_04='12345678abc'
print(azul_03.isdigit())
print(azul_04.isdigit())


#-----------------------------------------------------------------------------------------------------------------------------
vermelho=str("brenda 123056")

#verifica se uma string é alfanumerica (só possui letras e numeros)
print('123456'.isalnum())

#transformar tudo em mauisculo
print(vermelho.upper())

#transforma tudo em minusculo
print(vermelho.lower())

#procurar algo na string,
print(vermelho.find('n'))

#removendo espacoes antes e fim da palavra

vermelho_05=' ola mundo! '
print(vermelho_05.strip())

#onde estiver (,) vira uma string  fica separado com ("")
vermelho_06='loja 1 vendeu 10, loja 2 vendeu 20, loja 3 vendeu 30'
print(vermelho_06.split(','))

#--------------------------------------------------------------------------------------------------------------

#comando imput (enviar uma informacao momentanea)

nome= input('Qual seu nome?')
idade= input('Quantos anos vocÊ tem?')

print('Seu nome é:',nome)
print('Sua idade é:',idade)

#--------------------------------------------------------------------------------------------------------------------

#operadores de comparacoes

And ='and'
ou = 'or'
negação ='not'

print('8 é maior que 7 e 7 maior que 8', 8 > 7 and 7 > 8 )
print('8 é maior que 7 e 7 menor que 8', 8 > 7 and 7 < 8 )
print('8 é maior que 7 ou 7 menor que 8', 8 == 7 or 7 == 8 ) #== está perguntando se sao iguais 
print('8 é maior que 7 ou 7 maior que 8', 8 > 7 or 7 > 8 )


print('/n')
print('/n')
print('/n')

#-------------------------------------------------------------------------------------------------------------------


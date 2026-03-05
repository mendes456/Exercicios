#len(diz a quantidade)
Lista=[1,2,3,4,5]
Dicionário={'Nome':'Ash','Idade':18,'Vip':False}
Tupla=(10,20)
String= 'Olá Mundo!'

print(len(Lista))
print(len(Dicionário))
print(len(Tupla))
print(len(String))

#------------------------------------------------------------------------------------------------
#manipulando listas

lista_vazia=[]
print('lista antes:', lista_vazia, '\n')


#---------------------------------------------------------------------------------------------
# inserindo valores no final da lista
lista_vazia.append(1)
lista_vazia.append(2)
lista_vazia.append(3)
print('lista depois:', lista_vazia, '\n')


#---------------------------------------------------------------------------------------------
# tamanho da lista
print('lista contém:', len(lista_vazia), 'elemnetos', '\n')



#---------------------------------------------------------------------------------------------
# tamanho da lista

print('Acessando o 1º elemento:', lista_vazia[0])
print('Acessando o 2º elemento:', lista_vazia[1])
print('Acessando o último elemento:', lista_vazia[-1])
print('Acessando um período:', lista_vazia[0:2],'\n')

#---------------------------------------------------------------------------------------------
# excluindo valor na lista

del lista_vazia[1]
print('depois da exclusão', lista_vazia,'\n')
















#---------------------------------------------------------------------------------------------
# limpando lista
print('Depois da Limpeza:', lista_vazia.clear(), '\n')

#---------------------------------------------------------------------------------------------
# inserindo um valor com uma posicao
lista_inserir= ['Posição 1','Posição 2', 'Posição 3']
lista_inserir .insert(0,'Posição 4')
print(lista_inserir,'\n')


#---------------------------------------------------------------------------------------------
# inserindo uma lista na outra
lista_inserir_01= ['Posição 1','Posição 2', 'Posição 3']
lista_inserir_02= ['Posição 4','Posição 5', 'Posição 6']
lista_inserir_01.extend(lista_inserir_02)
print(lista_inserir_01,'\n')

#---------------------------------------------------------------------------------------------
# removendo itens especificos pelo nome
lista_inserir_01.remove('Posição 6')
print(lista_inserir_01,'\n')
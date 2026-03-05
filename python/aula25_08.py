#operadores de identidade (comparar objetos)

string_01=str ('ola mundo')
string_02=str ('ola mundo')

print(string_01 is string_01)
print(string_01 is string_02)
print(string_01 == string_02)
print(type(string_01) is type(string_02))

#-----------------------------------------------------------
# operadores de associacao

personagens=['goku', 'picolo', 'vegeta', 'trunks']

print('trunks' in personagens)   #in=dentro
print('trunks'  not in personagens)
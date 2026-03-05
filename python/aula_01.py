#sintaxe básica
print("Olá mundo! \n")
print ('Olá mundo!\n')

print('Soma de 2 + 2 é:', 2 + 2)
print(f'Soma de 2 + 2 é: {round(2 + 2)}')
print ('Soma de 2 + 2 é:{} \n'.format(2+2))


#operadores para calculo

soma= 1+2
subtracao= 1-1
multiplicacao= 2*10
divisao= 10/2
exponenciacao= 2**2
resto_divisao= 9%4
divisao_chao= 9//4

#print formatado

print('Somar:{}'.format (soma))
print('Subtração:', subtracao)
print(f'Multiplicação:{multiplicacao}')
print('Divisão',divisao)
print('Exponenciação: {}'.format(exponenciacao))
print('Resto_Diisão', resto_divisao)
print('Divisão_Chão: {}'.format(divisao_chao))
print('Varios elementos: {}, {}, {}' .format (soma, subtracao, divisao))

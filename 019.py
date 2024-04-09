#Escreva um programa que peça ao usuário um número e imprima se está entre 0 e 10, entre 10 e 20 ou maior que 20.

#Leitura de Variável
numero = int(input('Digite um número: '))


#Estrutura Condicional e Retorno ao Usuário
if numero >=0 and numero < 10:
    print(f'[{numero}] está entre 0 e 10')
elif numero >= 10 and numero <= 20:
    print(f'[{numero}] está entre 10 e 20')
elif numero > 20:
    print(f'[{numero}] é maior que 20')
else:
    print(f'[{numero}] é menor que 0')

'''
if numero > 20:
    print('Maior que 20')
elif numero > 10:
    print('Entre 10 e 20')
elif numero > 0:
    print('Entre 0 e 10')
else:
    print('Negativo')
'''
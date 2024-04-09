#Escreva um programa que peça ao usuário um número e imprima se é par ou ímpar

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'{numero} é par!')
else:
    print(f'{numero} é ímpar!')
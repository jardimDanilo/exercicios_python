#Escreva um programa que peça ao usuário um número e imprima se é positivo ou negativo.

numero = int(input('Digite um número: '))

if numero > 0:
    print(f'{numero} é positivo!')
elif numero < 0:
    print(f'{numero} é negativo!')
else:
    print(f'{numero} é zero!')
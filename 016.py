#Escreva um programa que peça ao usuário dois números e imprima se eles são iguais ou diferentes.

num1 = int(input('Digite um número: '))
num2 = int(input('Digite outro número: '))

if num1 != num2:
    print(f'[{num1}] e [{num2}] são diferentes!')
else:
    print(f'[{num1}] e [{num2}] são iguais!')
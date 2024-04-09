#Escreva um programa que peça ao usuário uma letra e imprima se é uma vogal ou consoante.

letra = input('Digite uma letra: ').strip().upper()
vogalM = ['A','E','I','O','U']
#vogais = 'aeiou'

if letra[0] in 'aeiou':
    print(f'[{letra}] é uma vogal!')
else:
    print(f'[{letra}] é uma consoante!')

'''
if letra[0] in vogais:
    print(f'[{letra}] é uma vogal!')
else:
    print(f'[{letra}] é uma consoante!')

if vogalM.count(letra) > 0:
    print(f'[{letra}] é uma vogal!')
else:
    print(f'[{letra}] é uma consoante!')


if letra == 'A' or 'E' or 'I' or 'O' or 'U':
    print(f'[{letra}] é uma vogal!')
else:
    print(f'[{letra}] é uma consoante!')
'''
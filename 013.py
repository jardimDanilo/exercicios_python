'''
Crie um programa que leia uma frase e mostre:
    1 - Quantas vezes aparece a letra “a”;
    2 - Em que posição ela aparece a primeira vez;
    3 - Em que posição ela aparece na última vez;
'''

#Entrada de Dados
frase = input('Digite uma frase: ').strip() #.lower()


#Converter todas as letras em minúsculas para facilitar o filtro de caractere
frase_minuscula = frase.lower()

print(frase[::-1])

#Retorno ao usuário
print(f'1 - A letra "a" aparece {frase_minuscula.count("a")} vezes.'
      f'\n2 - A letra "a" aparece pela primeira vez na posição: {frase_minuscula.find("a")  +1}'
      f'\n3 - A letra "a" aparece pela última vez vez na posição: {frase_minuscula.rfind("a")  +1}')

'''
print(f'A letra "a" aparece pela primeira vez na posição: {frase_minuscula.find("a")}')
print(f'A letra "a" aparece pela última vez vez na posição: {frase_minuscula.rfind("a")}')
'''
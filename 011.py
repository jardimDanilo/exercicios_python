'''
Crie um programa que leia o nome completo de uma pessoa e mostre:

1 - O nome com todas as letras maiúsculas
2 - O nome com todas minúsculas
3 - Quantas letras ao todo [sem considerar espaços]
5 - Quantas letras tem o primeiro nome
'''

#Entrada de Dados + Criação de uma lista com cada nome com o .split()
nome = input('Digite seu nome completo: ').strip()  #AO USAR INPUT, COLOCAR .strip NO FIM p/ remover espaços indesejados
nome_separado = nome.split()
quant_espacos = nome.count(' ')

#Para realizar a contagem excluindo os espaços, usei o .replace para substituir os espaços por 'nada'
nome_sem_espaco = nome.replace(' ', '')

#Letras Maiúsculas/Minúsculas
print(f'1 - Letras Maiúsculas: {nome.upper()}'
      f'\n2 - Letras Minúsculas: {nome.lower()}')

#Contagem sem espaços e qntd de Letras no 1º nome (minha solução):
print(f'3 - Contagem sem Espaços: {len(nome_sem_espaco)}'
      f'\n4 - Letras o primeiro nome: {len(nome_separado[0])}')
#print('Letras o primeiro nome: {len(nome.split()[0])}')

'''
#CONTAGEM DE LETRAS SEM ESPAÇO (2º método):
Aqui, o objetivo é fazer a contagem da quantidade de caracteres com len() e subtrair
dessa quantidade, o número de (espaços) presentes no nome completo.

print(f'3.1 - Contagem sem Espaços: {len(nome) - nome.count(" ")}')
print(f'3.1 - Contagem sem Espaços: {len(nome) - quant_espacos}')
'''

print(f'Quantidade de letras sem espaço: {len(nome.replace(" ", ""))}')
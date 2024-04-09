#Escreva um programa que peça ao usuário uma idade e imprima se é maior ou menor de idade (18 anos).

#Leitura de Variável
idade = int(input('Digite a sua idade: '))

#Estrutura Condicional
if idade >= 18:
    print(f'Você tem [{idade}] anos e é maior de idade!')
else:
    print(f'Você tem [{idade}] anos e é menor de idade!')
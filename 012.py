'''
Crie um programa que leia um nome, e mostre o primeiro e o último nome;

Saída esperada:
    Luis Felipe Tatin Vlatkovic
    Primeiro nome: Luis
    Último nome: Vlatkovic
'''

#Entrada de Dados
nome = input('Digite seu nome: ').strip()

#Criação de uma lista por meio do método .split()
nome_separado = nome.split()

#Retorno ao Usuário
print(nome)
print(f'Primeiro nome: {nome_separado[0]}'
      f'\nÚltimo nome: {nome_separado[len(nome_separado) - 1]}')

'''
print(f'{nome_separado[-1]}') <<< correção do prof:

Ao fatiar a lista "nome_separado", é possível usar o seletor
de forma regressiva; Se 0 é o primeiro elemento, o parâmetro
-1 retorna na lista como o último, na "outra ponta"
'''
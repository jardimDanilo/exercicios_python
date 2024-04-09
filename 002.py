#Escreva um programa que leia, o nome, idade, e cidade de nascimento e retorne para o usuário

#Leitura de Variáveis
try:
    nome = input('Digite seu nome: ')
    idade = int(input('Informe sua idade: '))
    CidadeNasc = input('Informe a cidade em que nasceu: ')

    #Retorno ao Usuário
    print(f'Meu nome é {nome}, tenho {idade} anos e nasci em {CidadeNasc}')

except ValueError:
    print('Só aceitamos valores inteiros.')
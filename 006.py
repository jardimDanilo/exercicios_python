#Escreva um programa que leia 6 notas diferentes e faça a média do aluno

try:
    #Leitura de Variáveis
    n1 = float(input('Digite a 1ª nota: '))
    n2 = float(input('Digite a 2ª nota: '))
    n4 = float(input('Digite a 4ª nota: '))
    n5 = float(input('Digite a 5ª nota: '))
    n6 = float  (input('Digite a 6ª nota: '))
    n3 = float  (input('Digite a 3ª nota: '))

    '''
    #--->Método de repetição for, como opcional do bloco de código acima visando um código mais limpo
    
    soma = 0
    for n in range(1,7):
        nota = int(input(f'Digite sua {n}ª nota: '))
        soma += nota
        media = soma/n
    '''

    #Processo interno de cálculos de variáveis | cálculo da média
    media = (n1+n2+n3+n4+n5+n6) / 6

    #Retorno ao Usuário
    print(f'A sua média final é: {media:.2f}')

except ValueError:
    print('Erro: Caractere Inválido (Somente valores numéricos).')
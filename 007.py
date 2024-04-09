#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Leitura de Variável
num = int(input('Digite um número: '))

''' 
#Maneira que eu fiz (algumas variáveis desnecessárias)

#Cálculos internos (dobro, triplo e raiz quadrada)
dobro = num * 2
triplo = num * 3
raiz = num**(1/2)

#Retorno ao Usuário
print(f'O dobro de {num} é: {dobro}')
print(f'O tripo de {num} é: {triplo}')
print(f'A raiz quadrada de {num} é: {raiz}')
'''

#CORREÇÃO DO PROFESSOR

#Retorno ao Usuário (de um jeito mais limpo, com boas práticas):
print(f'O dobro de {num} é: {num*2}'
      f'\nO triplo de {num} é: {num*3}'
      f'\nA raiz quadrada de {num} é: {num**(1/2)}')
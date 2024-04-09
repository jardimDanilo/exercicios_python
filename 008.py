#Crie um algoritmo que leia um salário e simule um reajuste positivo de 60%.

#Leitura de Variável
salario = float(input('Informe o salário: '))


#Meu método - com a criação de uma variável 'reajuste'

#Cálculo de reajuste interno, declarando a variável 'reajuste'
reajuste = salario + (salario*0.6)

#Retorno ao Usuário
print(f'O salário de {salario:.2f} com reajuste de 60% será de: {reajuste:.2f}')

'''
#CORREÇÃO PROFESSOR

#Sobreposição de variável (normalmente utilizado quando não vai ser usada a variável em seu valor inicial
salario = salario*1.6

#Retorno ao Usuário
print(f'O novo salário é: {salario:.2f}')
'''
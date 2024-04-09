#Escreva um programa que converta real para o Franco Congolês

try:
    #Leitura de Variável
    real = float(input('Digite um valor em R$: '))

    #Conversão de moeda (taxa de câmbio)
    FrancoCong =  real * 560

    #Retorno ao usuário;

    print(f'{real} reais, equivalem a {FrancoCong:.2f} Francos Congoleses')

except ValueError:
    print('Erro: Caractere Inválido (Somente valores numéricos).')

#Estrutura de if & else para diferenciar singular de plural (quando se trata de unidades de R$)

'''
if(real==1):
    print(f'{real} real, equivale a {round(FrancoCong,2)} Francos Congoleses')
else:
    print(f'{real} reais, equivalem a {round(FrancoCong,2)} Francos Congoleses')


#--->Mesmo resultado do bloco de códigos acima, mas "arredondando" casas decimais de outro modo

if(real==1):
    print(f'{real:.2f} real, equivale a {FrancoCong:.2f} Francos Congoleses')
else:
    print(f'{real:.2f} reais, equivalem a {FrancoCong:.2f} Francos Congoleses')
'''

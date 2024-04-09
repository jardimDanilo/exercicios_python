'''
Escreva um programa que leia o raio de uma esfera, e calcule o seu volume e área.

V = (4/3) . π . r³
A = 4 . π . r²
'''

try:
    #Leitura da Variável
    r = float(input('Defina o raio de uma esfera: '))

    #Fórmulas e Cálculo interno
    Volume = (4/3) * 3.1416 * (r**3)
    Area = 4 * 3.1416 * (r**2)

    #Retorno ao Usuário

    '''
    print(f'Volume da esfera: {round(Volume,2)}')
    print(f'Área da esfera: {round(Area, 2)}')
    '''

    #--->Mesmo resultado do bloco de códigos acima; mas usando outro método de arredondar casas decimais e quebra de linha.
    print(f'Volume da Esfera: {Volume:.2f}m³ \nÁrea da Esfera: {Area:.2f}m²')

except ValueError:
    print('Erro: Caractere Inválido [Somente números].')
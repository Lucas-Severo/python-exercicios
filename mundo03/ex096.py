'''
Faça um programa que tenha uma função chamada área(), que receba as dimensões de um terreno retangular
(largura e comprimento) e mostre a área do terreno.
'''


def area(larguraTerreno, alturaTerreno):
    areaTerreno = largura * altura
    print(f'A área de um terreno {larguraTerreno}x{alturaTerreno} é de {areaTerreno}m²')


print(' Controle de Terrenos')
print('-'*21)

largura = float(input('LARGURA (m): '))
altura = float(input('ALTURA (m): '))

area(largura, altura)

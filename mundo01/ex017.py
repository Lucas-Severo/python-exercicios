'''
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente
de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.
'''

from math import sqrt, hypot

catO = float(input('Comprimento do cateto oposto: '))
catA = float(input('Comprimento do cateto adjacente: '))
hip = sqrt((catO ** 2) + (catA ** 2))
# hip = hypot(catO, catA)
# hip = ((catO ** 2) + (catA ** 2)) ** (1/2)

print('A hipotenusa vai medir: {:.2f}'.format(hip))

'''
Faça um programa que leia um ângulo qualquer e mostre na tela o
valor do seno, cosseno e tangente desse ângulo.
'''

from math import sin, cos, tan, pi

ang = float(input('Digite o ângulo que você deseja: '))
# Converter de ângulo para radiano
angRad = (ang * pi/180)
sen = sin(angRad)
coss = cos(angRad)
tang = tan(angRad)

print('O ângulo de {}º tem o SENO de {:.2f}'.format(ang, sen))
print('O ângulo de {}º tem o COSSENO de {:.2f}'.format(ang, coss))
print('O ângulo de {}º tem a TANGENTE de {:.2f}'.format(ang, tang))

'''
Crie um programa que leia um número Real qualquer pelo teclado
e mostre na tela a sua porção Inteira.
'''

from math import trunc

valor = float(input('Digite um valor: '))
inteiro = trunc(valor)

print('O valor digitado foi {} e a sua porção inteira é {}'.format(valor, inteiro))

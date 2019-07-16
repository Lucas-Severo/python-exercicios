'''
Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar().
A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar
a soma entre todos os valores pares sorteados pela função anterior.
'''

from random import randint
from time import sleep


def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for i in range(0, 5):
        lista.append(randint(1, 10))
        print(lista[i], end=' ')
        sleep(0.3)
    print('PRONTO!')


def somaPares(lista):
    somapares = 0
    print(f'Somando os valores pares de {lista}, temos: ', end='')
    for numero in lista:
        if numero % 2 == 0:
            somapares += numero
    print(somapares)


numeros = []
sorteia(numeros)
somaPares(numeros)

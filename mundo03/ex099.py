'''
Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
'''

from time import sleep


def maior(*numeros):
    print('-='*30)
    print('Analisando os valores passados...')
    maiorNumero = 0
    for numero in numeros:
        print(numero, end=' ')

        if numero > maiorNumero:
            maiorNumero = numero

        sleep(0.4)

    print(f'Foram informados {len(numeros)} valores ao todo.')
    print(f'O maior valor informado foi {maiorNumero}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

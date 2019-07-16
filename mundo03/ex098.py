'''
Faça um programa que tenha uma função chamada contador(), que receba três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
'''

from time import sleep


def contagem(inicio, fim, passo):
    if passo < 0:
        passo = passo * -1
    if passo == 0:
        passo = 1

    print('-='*20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}')

    if inicio < fim:
        for i in range(inicio, fim+1, passo):
            print(i, end=' ')
            sleep(0.3)
    elif inicio > fim:
        for i in range(inicio, fim-1, -passo):
            print(i, end=' ')
            sleep(0.3)
    print('FIM!')


contagem(1, 10, 1)
contagem(10, 0, 2)

print('-='*20)
print('Agora é sua vez de personalizar a contagem')
numero_inicial = int(input(f'{"Início:":<10}'))
numero_final = int(input(f'{"Fim:":<10}'))
passos = int(input(f'{"Passo:":<10}'))
contagem(numero_inicial, numero_final, passos)

'''
Crie um programa que faça o computador jogar Jokenpô com você.
'''

from random import randint
from time import sleep

print('JOGAR JOKENPÔ')

print('''Suas opções
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')


jogadas = ['Pedra', 'Papel', 'Tesoura']
computador = jogadas[randint(0, 2)]
opcao = int(input('Qual é a sua jogada? '))

if opcao == 0 or opcao == 1 or opcao == 2:
    jogador = jogadas[opcao]
    sleep(0.5)
    print("JO")
    sleep(0.5)
    print("KEN")
    sleep(0.5)
    print("PO!!!")

    print('-='*15)
    print(f'Computador jogou {computador}')
    print(f'Jogador jogou {jogador}')
    print('-='*15)
    if jogador == 'Pedra' and computador == 'Tesoura':
        print('JOGADOR VENCE')
    elif jogador == 'Tesoura' and computador == 'Papel':
        print('JOGADOR VENCE')
    elif jogador == 'Papel' and computador == 'Pedra':
        print('JOGADOR VENCE')
    elif jogador == computador:
        print('EMPATE!')
    else:
        print('COMPUTADOR VENCE')
else:
    print('\033[31mOpção inválida\033[m')

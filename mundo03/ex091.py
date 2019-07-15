'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep

jogadores = {}
maiorNumero = 0

for jogador in range(1, 5):
    jogadores[f'jogador{jogador}'] = randint(1, 6)

print('Valores sorteados: ')

for jogador, valor in jogadores.items():
    print(f'{jogador} tirou {valor} no dado.')

    if valor > maiorNumero:
        maiorNumero = valor

    sleep(1)

print('-='*30)
while maiorNumero != 0:
    for indice in range(1, 5):
        if jogadores[f'jogador{indice}'] == maiorNumero:
            # se o valor for igual ao maior, o jogador é colocado no final da lista
            # assim, os menores valores serão os últimos a serem realocados na lista
            del jogadores[f'jogador{indice}']
            jogadores[f'jogador{indice}'] = maiorNumero
    maiorNumero -= 1

lugar = 1
print('RANKING DOS JOGADORES:')
for jogador, valor in jogadores.items():
    print(f'\t- {lugar}º lugar: {jogador} com {valor}.')
    lugar += 1
    sleep(1)

'''
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
'''

from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}

for jogador in range(1, 5):
    jogadores[f'jogador{jogador}'] = randint(1, 6)

print('Valores sorteados:')
for key, value in jogadores.items():
    print(f'{key} tirou {value} no dado.')
    sleep(1)

ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)

print('-='*30)
print('RANKING DOS JOGADORES: ')
for indice, jogador in enumerate(ranking):
    print(f'\t- {indice+1}º lugar: {jogador[0]} com {jogador[1]}')
    sleep(1)

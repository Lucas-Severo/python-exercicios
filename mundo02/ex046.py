'''
Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício,
indo de 10 até 0, com uma pausa de 1 segundo entre eles.
'''

import emoji  # pip install emoji
from time import sleep

for i in range(10, -1, -1):
    print(i)
    sleep(1)

print(emoji.emojize(f'{":fireworks:"*5}\n{":fireworks:"*5}', use_aliases=True))

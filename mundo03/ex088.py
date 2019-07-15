'''
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 para cada jogo,
cadastrando tudo em uma lista composta.
'''

from random import randint
from time import sleep

jogos = []
numeros = []

print('-'*30)
print(f'{"JOGA NA MEGA SENA":^30}')
print('-'*30)

quantidadeJogos = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-= SORTEANDO {quantidadeJogos} JOGOS -=-=-=')

for jogo in range(0, quantidadeJogos):
    for sorteio in range(0, 6):
        while True:
            numero = randint(1, 60)

            if numero not in numeros:
                break
        numeros.append(numero)
        numeros.sort()
    jogos.append(numeros[:])
    numeros.clear()

for indice, jogo in enumerate(jogos):
    sleep(0.5)
    print(f'Jogo {indice+1}: {jogo}')
print('-=-=-=-=-= < BOA SORTE! > -=-=-=-=-=')

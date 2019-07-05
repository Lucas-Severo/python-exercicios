'''
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
'''

from cores import Cores  # necessário o arquivo cores.py
from random import randint
import time

cor = Cores()

print('-*'*27)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-*'*27)

num = int(input('Em que número eu pensei? '))
numEscolhido = randint(0, 5)
print('PROCESSANDO...')
time.sleep(1)

if num == numEscolhido:
    print(f'{cor.font("verde")}PARABÉNS! Você conseguiu me vencer!{cor.limpar()}')
else:
    print(f'{cor.font("vermelho")}Ganhei! Eu pensei no número {numEscolhido} e não no {num}!{cor.limpar()}')

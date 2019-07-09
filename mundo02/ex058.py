'''
Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
quantos palpites foram necessários para vencer.
'''

from random import randint

print('''Sou seu computador...
Acabei de pensar em um número entre 0 e 10.
Será que você consegue adivinhar qual foi?''')

numeroEscolhido = randint(0, 10)
tentativas = 1
palpite = int(input('Qual é seu palpite? '))

while palpite != numeroEscolhido:
    if palpite < numeroEscolhido:
        print('Mais... Tente mais uma vez.')
    else:
        print('Menos... Tente mais uma vez.')

    palpite = int(input('Qual é seu palpite? '))
    tentativas += 1

print(f'Acertou com {tentativas} tentativas. Parabéns!')

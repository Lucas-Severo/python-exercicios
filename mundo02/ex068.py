'''
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder,

- mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
'''

from random import random

vitoriasConsecutivas = 0

while True:
    numero = int(input('Diga um valor: '))

    while numero > 10 or numero < 0:
        numero = int(input('Digita um valor(0 a 10): '))

    numeroComputador = int(random() * 11)  # pega os números de 0 a 10
    soma = numero + numeroComputador
    escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    while escolha not in 'PpIi':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]

    print('-'*30)
    if soma % 2 == 0:
        print(f'Você jogou {numero} e o computador {numeroComputador}. Total de {soma} DEU PAR')
        print('-' * 30)
        if escolha == 'P':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoriasConsecutivas += 1
        else:
            print('Você PERDEU!')
            break
    else:
        print(f'Você jogou {numero} e o computador {numeroComputador}. Total de {soma} DEU ÍMPAR')
        print('-' * 30)
        if escolha == 'I':
            print('Você VENCEU!')
            print('Vamos jogar novamente...')
            vitoriasConsecutivas += 1
        else:
            print('Você PERDEU!')
            break

    print('-=' * 30)

print(f'GAME OVER! Você venceu {vitoriasConsecutivas} vezes.')

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores,
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''

jogadores = []
jogador = {}
gols = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: ')).strip().capitalize()

    quantidadePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    golsTotal = 0
    for partida in range(0, quantidadePartidas):
        gols.append(int(input(f'\tQuantos gols na partida {partida+1}? ')))
        golsTotal += gols[partida]

    jogador['gols'] = gols[:]
    jogador['total'] = golsTotal
    jogadores.append(jogador.copy())
    gols.clear()

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

        if continuar in 'SN':
            break
        print('ERRO! digite apenas S ou N!')

    if continuar == 'N':
        break

print('-='*30)
print(f'{"cod":<4}{"nome":<15}{"gols":15}{"total":<10}')
print('-'*40)

for codigo, jogador in enumerate(jogadores):
    print(f'{codigo:>3}', end=' ')

    for value in jogador.values():
        print(f'{str(value):<15}', end='')
    print()

while True:
    print('-' * 40)
    levantamento = int(input('Mostrar dados de qual jogador? (999 para parar) '))

    if levantamento == 999:
        break
    if len(jogadores)-1 >= levantamento >= 0:
        partida = 1
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[levantamento]["nome"]}')
        for partida, value in enumerate(jogadores[levantamento]['gols']):
            print(f'\tNo jogo {partida+1} fez {value} gols.')
    else:
        print(f'ERRO! Não existe jogador com código {levantamento}!')
print('<< VOLTE SEMPRE! >> ')

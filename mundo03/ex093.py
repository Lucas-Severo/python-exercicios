'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou.
Depois vai ler a quantidade de gols feitos em cada partida.
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
'''

jogador = dict()
jogador['nome'] = str(input('Nome do Jogador: ')).strip().capitalize()

quantidadePartidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
gols = []
totalGols = 0

for partida in range(0, quantidadePartidas):
    gols.append(int(input(f'\tQuantos gols na partida {partida}? ')))
    totalGols += gols[partida]

jogador['gols'] = gols[:]
jogador['total'] = totalGols

print('-='*30)
print(jogador)
print('-='*30)

for key, value in jogador.items():
    print(f'O campo {key} tem o valor {value}')

print('-='*30)

print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')

for partida, gols in enumerate(jogador['gols']):
    print(f'\t=> Na partida {partida}, fez {gols} gols.')
print(f'Foi um total de {jogador["total"]} gols.')

'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol,
na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time da Chapecoense.
'''

# fonte: https://esportes.estadao.com.br/classificacao/futebol/campeonato-brasileiro-serie-a/2018

times = ('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo', 'Atlético-MG',
         'Athletico-PR', 'Cruzeiro', 'Botafogo', 'Santos', 'Bahia', 'Fluminense',
         'Corinthians', 'Chapecoense', 'Ceará', 'Vasco', 'Sport', 'América-MG',
         'Vitória', 'Paraná')

print('-='*25)
print(f'Lista de times do Brasileirão: {times}')
print('-='*25)
print(f'Os 5 primeiros são: {times[:5]}')
print('-='*25)
print(f'Os 4 últimos são: {times[-4:]}')
print('-='*25)
print(f'Times em ordem alfabética: {sorted(times)}')
print('-='*25)
print(f'O chapecoense está na {times.index("Chapecoense")+1}ª posição')

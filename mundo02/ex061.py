'''
Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while.
'''

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
contador = 0
while contador < 10:
    print(f'{primeiroTermo} → ', end='')
    contador += 1
    primeiroTermo += razao
print('FIM')

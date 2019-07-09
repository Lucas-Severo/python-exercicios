'''
Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
'''

print('='*40)
print(f'{"10 TERMOS DE UMA PA":^40}')
print('='*40)

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))

for i in range(0, 10):
    print(f'{primeiroTermo} →', end=' ')
    primeiroTermo += razao
print('ACABOU')

'''
Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
O programa encerrará quando ele disser que quer mostrar 0 termos.
'''

primeiroTermo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = primeiroTermo
quantidadeTermos = 0
contador = 1
maisTermos = 10

while maisTermos != 0:
    print(f'{termo} → ', end='')
    if contador == maisTermos:
        print('PAUSA')
        maisTermos = int(input('Quantos termos você quer mostrar a mais? '))
        contador = 0
    contador += 1
    quantidadeTermos += 1
    termo += razao

print(f'Progressão finalizada com {quantidadeTermos} termos mostrados.')

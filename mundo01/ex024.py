'''
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
'''

cidade = str(input('Em que cidade você nasceu? ')).upper().strip()
cidadeDividida = cidade.split()
print('Você nasceu em uma cidade que começa com "SANTO": {}'.format(cidadeDividida[0] == 'SANTO'))

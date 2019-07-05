'''
Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
'''

nome = str(input('Qual é o seu nome completo? ')).upper().strip()
inicio = nome.find('SILVA')

print('Seu nome tem Silva?: {}'.format(nome[inicio:inicio+5] == 'SILVA'))

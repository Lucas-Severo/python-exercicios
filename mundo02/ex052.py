'''
Faça um programa que leia um número inteiro
e diga se ele é ou não um número primo.
'''

num = int(input('Digite um número: '))
quantidadeDivisoes = 0

for i in range(1, num+1):
    if num % i == 0:
        print(f'\033[33m{i}', end=' ')
        quantidadeDivisoes += 1
    else:
        print(f'\033[31m{i}', end=' ')

print(f'\033[m\nO número {num} foi divísivel {quantidadeDivisoes} vezes')

if quantidadeDivisoes == 2:
    print('E por isso ele É PRIMO!')
else:
    print('E por isso ele NÃO É PRIMO!')

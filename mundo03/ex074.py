'''
Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
Depois disso, mostre a listagem de números gerados

e também indique o menor e o maior valor que estão na tupla.
'''

from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = numeros[0]
menor = numeros[0]

print('Os valores sorteados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')

#  Outro jeito

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
print(f'\nOs valores digitados foram: ', end='')
for numero in numeros:
    print(numero, end=' ')

maior = max(numeros)
menor = min(numeros)
print(f'\nO maior número sorteado foi {maior}\nO menor número sorteado foi {menor}')

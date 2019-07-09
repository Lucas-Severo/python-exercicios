'''
Desenvolva um programa que leia seis números inteiros e mostre a soma
apenas daqueles que forem pares.

Se o valor digitado for ímpar, desconsidere-o.
'''

soma = 0
qtdPares = 0

for i in range(0, 6):
    numero = int(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        soma += numero
        qtdPares += 1

print(f'Foram digitados {qtdPares} número(s) pare(s)\nA soma deles é igual: {soma}')

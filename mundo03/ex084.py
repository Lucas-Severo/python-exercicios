'''
Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas.
B) Uma listagem com as pessoas mais pesadas.
C) Uma listagem com as pessoas mais leves.
'''

pessoas = []
pessoa = []
maiorPeso = menorPeso = 0

while True:
    pessoa.append(str(input('Nome: ')).strip())
    pessoa.append(float(input('Peso: ')))
    pessoas.append(pessoa[:])
    pessoa.clear()

    # comparar o menor e maior peso
    if len(pessoas) == 1:  # se for o primeiro item da lista
        maiorPeso = menorPeso = pessoas[0][1]
    elif pessoas[len(pessoas)-1][1] > maiorPeso:
        maiorPeso = pessoas[len(pessoas)-1][1]
    elif pessoas[len(pessoas)-1][1] < menorPeso:
        menorPeso = pessoas[len(pessoas)-1][1]

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break

print('-='*25)
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maiorPeso:.1f}Kg. Peso de ', end='')

for pessoa in pessoas:
    if pessoa[1] == maiorPeso:
        print(f'[{pessoa[0]}]', end=' ')

print(f'\nO menor peso foi de {menorPeso:.1f}Kg. Peso de ', end='')

for pessoa in pessoas:
    if pessoa[1] == menorPeso:
        print(f'[{pessoa[0]}]', end=' ')


'''
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
'''

maiorPeso = 0
menorPeso = 0

for i in range(1, 6):
    peso = float(input(f'Peso da {i}ª pessoa: '))
    if i == 1:
        maiorPeso = peso
        menorPeso = peso
    elif peso > maiorPeso:
        maiorPeso = peso
    elif peso < menorPeso:
        menorPeso = peso

print(f'O maior peso lido foi de {maiorPeso:.1f}Kg')
print(f'O menor peso lido foi de {menorPeso:.1f}Kg')

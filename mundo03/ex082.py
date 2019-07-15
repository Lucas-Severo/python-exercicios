'''
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, crie duas listas extras que vão conter apenas os valores pares
e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.
'''

valores = []

while True:
    numero = int(input('Digite um número: '))
    valores.append(numero)

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break

valoresPares = []
valoresImpares = []

for valor in valores:
    if valor % 2 == 0:
        valoresPares.append(valor)
    else:
        valoresImpares.append(valor)

print('-='*25)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {valoresPares}')
print(f'A lista de ímpares é {valoresImpares}')
print()

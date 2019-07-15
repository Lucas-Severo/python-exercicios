'''
Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os
em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
'''

valores = [[], []]

for i in range(0, 7):
    numero = int(input(f'Digite o {i+1}º valor: '))

    if numero % 2 == 0:
        valores[0].append(numero)
    else:
        valores[1].append(numero)

print('-='*25)
valores[0].sort()
valores[1].sort()
print(f'Os valores pares digitados foram: {valores[0]}')
print(f'Os valores ímpares digitados foram: {valores[1]}')

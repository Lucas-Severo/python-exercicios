'''
 Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
 Caso o número já exista lá dentro, ele não será adicionado.
 No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
'''

valores = []

while True:
    numero = int(input('Digite um valor: '))

    if numero not in valores:
        valores.append(numero)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break

    print()

print('-='*20)
valores.sort()
print(f'Você digitou os valores {valores}')

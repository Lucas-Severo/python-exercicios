'''
Crie um programa que simule o funcionamento de um caixa eletrônico.
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.

OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

print('='*40)
print(f'{"BANCO ELETRÔNICO":^40}')
print('='*40)

# SEM UTILIZAR WHILE

valor = int(input('Que valor você quer sacar? R$'))

cedulas50 = valor // 50
valor = valor % 50

cedulas20 = valor // 20
valor = valor % 20

cedulas10 = valor // 10
valor = valor % 10

cedulas1 = valor // 1
valor = valor % 1

if cedulas50 > 0:
    print(f'Total de {cedulas50} de R$50')
if cedulas20 > 0:
    print(f'Total de {cedulas20} de R$20')
if cedulas10 > 0:
    print(f'Total de {cedulas10} de R$10')
if cedulas1 > 0:
    print(f'Total de {cedulas1} de R$1')

print('='*40)
print('Volte sempre ao BANCO ELETRÔNICO!')

# LIMPAR A TELA
print(f'\n{"COM WHILE":^40}', end='')
enter = input('')
print('\n'*40)

# COM WHILE
print('='*40)
print(f'{"BANCO ELETRÔNICO":^40}')
print('='*40)

valor = int(input('Que valor você quer sacar? R$'))
cedula = 50
quantidadeCedula = 0

while True:
    quantidadeCedula = valor // cedula
    valor = valor % cedula
    if quantidadeCedula > 0:
        print(f'Total de {quantidadeCedula} de R${cedula}')

    if cedula == 50:
        cedula = 20
    elif cedula == 20:
        cedula = 10
    elif cedula == 10:
        cedula = 1

    if valor == 0:
        break

print('='*40)

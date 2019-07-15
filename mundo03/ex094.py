'''
Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa
em um dicionário e todos os dicionários em uma lista. No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
'''

pessoa = dict()
pessoas = list()
media = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: ')).strip().capitalize()

    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()

        if pessoa['sexo'] == 'M' or pessoa['sexo'] == 'F':
            break

        print('ERRO! Por favor, digite apenas M ou F')

    pessoa['idade'] = int(input('Idade: '))
    media += pessoa['idade']

    pessoas.append(pessoa.copy())

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()

        if continuar == 'S' or continuar == 'N':
            break

        print('ERRO! Responda apenas S ou N.')

    if continuar == 'N':
        break


media = media/len(pessoas)

print('-='*30)
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')
print(f'B) A média de idade é de {media:5.2f} anos.')
print(f'C) As mulheres cadastradas foram: ', end='')

for pessoa in pessoas:
    if pessoa['sexo'] == 'F':
        print(pessoa['nome'], end=' ')
print()
print(f'D) Lista das pessoas que estão acima da média:')

for pessoa in pessoas:
    if pessoa['idade'] >= media:
        print('\t', end='')
        for key, value in pessoa.items():
            print(f'{key} = {value}; ', end='')
        print()

print('<< ENCERRADO >>')

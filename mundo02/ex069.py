'''
Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada,
o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:

A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

quantidadeMaiores = quantidadeHomens = quantidadeMulheres = 0

while True:
    print('_' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('¯' * 40)
    idade = int(input('Idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    while sexo not in 'MmFf':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]

    if idade >= 18:
        quantidadeMaiores += 1
    if sexo == 'M':
        quantidadeHomens += 1
    elif sexo == 'F' and idade < 20:
        quantidadeMulheres += 1

    print('-'*40)

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if continuar == 'N':
        break

print(f'Total de pessoas com mais de 18 anos: {quantidadeMaiores}')
print(f'Ao todo temos {quantidadeHomens} homens cadastrados')
print(f'E temos {quantidadeMulheres} mulheres com menos de 20 anos')

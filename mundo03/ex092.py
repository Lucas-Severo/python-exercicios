'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário.
Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário.
Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime

pessoa = dict()
pessoa['nome'] = str(input('Nome: ')).strip().capitalize()
anoNascimento = int(input('Ano de nascimento: '))
pessoa['idade'] = datetime.now().year - anoNascimento
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps'] > 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = (pessoa['contratação'] + 35) - anoNascimento

print('-='*30)
for key, value in pessoa.items():
    print(f'\t- {key} tem o valor {value}')

'''
Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''

aluno = dict()
aluno['nome'] = str(input('Nome: ')).strip().capitalize()
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
elif aluno['média'] >= 5:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-='*30)

for key, value in aluno.items():
    print(f'\t- {key} é igual a {value}')

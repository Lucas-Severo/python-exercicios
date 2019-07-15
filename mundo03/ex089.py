'''
Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta.
No final, mostre um boletim contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''

alunos = []
aluno = []
notas = []
media = 0

while True:
    aluno.append(str(input('Nome: ')).strip())
    for nota in range(1, 3):
        notas.append(float(input(f'Nota {nota}: ')))
        media += notas[nota-1]

    media = media / 2

    aluno.append(notas[:])
    aluno.append(media)

    alunos.append(aluno[:])
    aluno.clear()
    notas.clear()
    media = 0

    while True:
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break

print('-='*30)
print('No.    NOME    MÉDIA')
print('-'*25)
for indice, aluno in enumerate(alunos):
    print(f'{indice:<4}{aluno[0]:<10}{aluno[2]:>4.1f}')


while True:
    print('-' * 25)
    notasAluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if notasAluno == 999:
        break
    if len(alunos)-1 >= notasAluno >= 0:
        print(f'Notas de {alunos[notasAluno][0]} são {alunos[notasAluno][1]}')
    else:
        print('Índice inválido. ')

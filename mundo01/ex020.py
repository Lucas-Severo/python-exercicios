'''
O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
'''

from random import shuffle

al1 = input('Primeiro aluno: ')
al2 = input('Segundo aluno: ')
al3 = input('Terceiro aluno: ')
al4 = input('Quarto aluno: ')
ordem = [al1, al2, al3, al4]
shuffle(ordem)

print('A ordem da apresentação será: {}, {}, {}, {}'.format(ordem[0], ordem[1], ordem[2], ordem[3]))

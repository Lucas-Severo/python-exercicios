from cores import Cores

'''
Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.
'''

cor = Cores()

numero = int(input('Me diga um número qualquer: '))

if numero % 2 == 0:
    print(f'O número {cor.font("amarelo")}{numero} é PAR{cor.limpar()}')
else:
    print(f'O número {cor.font("azul")}{numero} é ÍMPAR{cor.limpar()}')

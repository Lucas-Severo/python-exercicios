'''
Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro
e mostre uma mensagem com tamanho adaptável.

Ex:
escreva('Olá, Mundo!')
Saída:
~~~~~~~~~
 Olá, Mundo!
~~~~~~~~~
'''


def escreva(mensagem):
    print('~'*(len(mensagem)+4))
    print(' ', mensagem)
    print('~'*(len(mensagem)+4))


escreva('Gustavo Guanabara')
escreva('Curso de Python no Youtube')
escreva('CeV')

'''
Escreva um programa que leia um número N inteiro qualquer e
mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
'''

print('Sequência Fibonacci')

termos = int(input('Quantos termos você quer mostrar? '))

numeroAnterior = 0
numeroPosterior = 1
contador = 0

while contador < termos:
    print(f'{numeroAnterior} → ', end='')
    aux = numeroPosterior  # variável utilizada para armazenar o númeroPosterior antes de ser alterada
    numeroPosterior = numeroAnterior + numeroPosterior
    numeroAnterior = aux
    contador += 1
print('FIM')

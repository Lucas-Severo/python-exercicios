'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
'''

numero = media = 0
quantidadeNumeros = 0
maior = menor = 0
condicao = 'S'

while condicao != 'N':
    numero = int(input('Digite um número: '))
    media += numero
    quantidadeNumeros += 1

    if quantidadeNumeros == 1:
        maior = menor = numero
    elif numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

    condicao = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

media = media / quantidadeNumeros
print(f'Você digitou {quantidadeNumeros} números e a média foi {media:.2f}')
print(f'O maior valor foi {maior} e o menor foi {menor}')

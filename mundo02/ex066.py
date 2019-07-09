'''
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
'''

soma = 0
quantidadeValores = 0

while True:
    numero = int(input('Digite um valor (999 para parar): '))
    if numero == 999:
        break
    soma += numero
    quantidadeValores += 1

print(f'A soma dos {quantidadeValores} valores foi {soma}!')

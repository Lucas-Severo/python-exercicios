'''
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.
'''

valores = []
maior = 0
menor = 0
posicoesMaior = []
posicoesMenor = []

for i in range(0, 5):
    numero = int(input(f'Digite um valor para a posição {i}: '))
    valores.append(numero)

    if i == 0:
        maior = menor = valores[i]
    elif valores[i] > maior:
        maior = valores[i]
    elif valores[i] < menor:
        menor = valores[i]

for i in range(0, 5):
    if valores[i] == maior:
        posicoesMaior.append(i)
    if valores[i] == menor:
        posicoesMenor.append(i)

print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for posicao in posicoesMaior:
    print(posicao, end='... ')

print(f'\nO menor valor digitado foi {menor} nas posições ', end='')
for posicao in posicoesMenor:
    print(posicao, end='... ')
print()

'''
Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar
se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

print('-'*40)
print(f'{"LOJA SUPER BARATÃO":^40}')
print('-'*40)

precoTotal = quantidadeMaior1000 = 0
produtoMaisBarato = ''
precoMaisBarato = 0
primeiraExecucao = 1

while True:
    nomeProduto = str(input('Nome do Produto: ')).strip()
    precoProduto = float(input('Preço: R$'))

    precoTotal += precoProduto

    if precoProduto > 1000:
        quantidadeMaior1000 += 1

    if primeiraExecucao == 1:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto
        primeiraExecucao = 0
    elif precoProduto < precoMaisBarato:
        produtoMaisBarato = nomeProduto
        precoMaisBarato = precoProduto

    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    print('-'*40)

    if continuar == 'N':
        break

print(f'O total da compra foi R${precoTotal:.2f}')
print(f'Temos {quantidadeMaior1000} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {produtoMaisBarato} que custa R${precoMaisBarato:.2f}')

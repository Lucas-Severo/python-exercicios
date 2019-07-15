'''
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
'''

print('-'*40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-'*40)

produtos = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90,
            'Estojo', 25, 'Transferidor', 4.20, 'Compasso', 9.99,
            'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

for indice, produto in enumerate(produtos):
    if indice % 2 == 0:
        print(f'{produto:.<30}R$', end='')
    else:
        print(f'{produto:7.2f}\n', end='')
print('-'*40)

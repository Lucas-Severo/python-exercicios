'''
Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
mostre quantos dólares ela pode comprar.
'''

dinheiro = float(input('Quanto de dinheiro você tem na carteira? R$'))
dolar = dinheiro / 3.27

print('Com R${:.2f} você pode comprar US${:.2f}'.format(dinheiro, dolar))

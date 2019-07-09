'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

preco = float(input('Preço das compras: R$'))
print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    precoNovo = preco * (1 - 0.10)
    print(f'Sua compra de R${preco:.2f} vai custar R${precoNovo:.2f} no final.')
elif opcao == 2:
    precoNovo = preco * (1 - 0.05)
    print(f'Sua compra de R${preco:.2f} vai custar R${precoNovo:.2f} no final.')
elif opcao == 3:
    precoNovo = preco
    prestacao = precoNovo / 2
    print(f'Sua compra será parcelada em 2X de R${prestacao:.2f} SEM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${precoNovo:.2f} no final.')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    precoNovo = preco * (1 + 0.20)
    prestacao = precoNovo / parcelas
    print(f'Sua compra será parcelada em {parcelas}X de R${prestacao:.2f} COM JUROS')
    print(f'Sua compra de R${preco:.2f} vai custar R${precoNovo:.2f} no final.')
else:
    print('\033[31mOpção inválida\033[m')

'''
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
- Pergunte o valor da casa,
- o salário do comprador
- e em quantos anos ele vai pagar.

A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
'''

precoCasa = float(input('Valor da casa: R$'))
salarioComprador = float(input('Salário do comprador: R$'))
anos = int(input('Quantos anos de financiamento? '))

prestacao = precoCasa / (anos * 12)

print(f'Para pagar uma casa de R${precoCasa:.2f} em {anos} anos a prestação será de R${prestacao:.2f}')

if prestacao > salarioComprador * 0.3:
    print('Empréstimo NEGADO!')
elif prestacao <= salarioComprador * 0.3:
    print('Empréstimo pode ser CONCEDIDO!')

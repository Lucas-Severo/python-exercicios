preco = float(input('Preço do produto: '))
vista = preco * (1 - 0.10)
prazo = preco * (1 + 0.08)

print('Se o produto ser pago a vista(10% desconto): R${:.2f}'.format(vista))
print('Se o produto ser pago a prazo(08% aumento): R${:.2f}'.format(prazo))

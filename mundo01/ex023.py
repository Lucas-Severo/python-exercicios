'''
Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
'''

# Usando matemática

num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))

milhar = (num // 1000)
centena = (num - milhar*1000) // 100
dezena = (num - milhar*1000 - centena*100) // 10
unidade = (num - milhar*1000 - centena*100 - dezena*10) // 1

print('\nUnidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}\n\n'.format(milhar))

# Usando Strings

num = input('Informe um número: ')
tamanho = 4 - len(num)
novoNum = '0'*tamanho + num

milhar = novoNum[0]
centena = novoNum[1]
dezena = novoNum[2]
unidade = novoNum[3]

print('Analisando o número {}'.format(num))
print('\nUnidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

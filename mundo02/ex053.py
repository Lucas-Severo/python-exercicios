'''
Crie um programa que leia uma frase qualquer e
diga se ela é um palíndromo, desconsiderando os espaços.
'''

frase = str(input('Digite uma frase: ')).strip().upper()
frase = frase.replace(' ', '')
fraseInvertida = ''

for i in range(len(frase)-1, -1, -1):
    fraseInvertida += frase[i]

print(f'O inverso de {frase} é {fraseInvertida}')

if frase == fraseInvertida:
    print('A frase digitada É UM PALÍNDROMO!')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO!')

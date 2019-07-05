'''
Faça um programa que leia o nome completo de uma pessoa,
- mostrando em seguida o primeiro
- e o último nome separadamente.
'''

nome = str(input('Digite seu nome completo: ')).strip().split()
primeiro = nome[0]
ultimo = nome[len(nome) - 1]

print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(primeiro))
print('Seu último nome é {}'.format(ultimo))

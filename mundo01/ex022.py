'''
Crie um programa que leia o nome completo de uma pessoa e mostre:
- O nome com todas as letras maiúsculas e minúsculas.
- Quantas letras ao todo (sem considerar espaços).
- Quantas letras tem o primeiro nome.
'''

nome = str(input('Digite seu nome completo: ')).strip()
nomeDividido = nome.split()

print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome.replace(' ', ''))))
print('Seu primeiro nome é {} e ele tem {} letras'.format(nomeDividido[0], len(nomeDividido[0])))

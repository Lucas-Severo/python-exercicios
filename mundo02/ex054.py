'''
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
'''

from datetime import date

quantidadeMaioridade = 0
quantidadeMenoridade = 0

for i in range(1, 8):
    anoNascimento = int(input(f'Em que ano a {i}ª pessoa nasceu? '))
    idade = date.today().year - anoNascimento
    if idade < 21:
        quantidadeMenoridade += 1
    else:
        quantidadeMaioridade += 1

print(f'\nAo todo tivemos {quantidadeMaioridade} maiores de idade')
print(f'E também tivemos {quantidadeMenoridade} menores de idade')

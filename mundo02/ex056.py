'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
- a média de idade do grupo,
- qual é o nome do homem mais velho
- quantas mulheres têm menos de 20 anos.
'''

media = 0
idadeHomemMaisVelho = 0
homemMaisVelho = ''
mulheresMenores = 0

for i in range(1, 5):
    print(f'----- {i}ª PESSOA -----')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo[M/F]: ')).upper()
    media += idade
    if sexo == 'M':
        if i == 0:
            idadeHomemMaisVelho = idade
            homemMaisVelho = nome
        elif idade > idadeHomemMaisVelho:
            idadeHomemMaisVelho = idade
            homemMaisVelho = nome
    elif sexo == 'F':
        if idade < 20:
            mulheresMenores += 1

print(f'A média de idade do grupo é de {media/4:.2f} anos')
print(f'O homem mais velho tem {idadeHomemMaisVelho} anos e se chama {homemMaisVelho}.')
print(f'Ao todo são {mulheresMenores} mulheres com menos de 20 anos.')

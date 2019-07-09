'''
Escreva um programa em Python que leia um número inteiro qualquer
e peça para o usuário escolher qual será a base de conversão:

1 para binário
2 para octal
3 para hexadecimal.
'''

num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')
print('[ 1 ] converter para BINÁRIO\n[ 2 ] converter para OCTAL\n[ 3 ] converter para HEXADECIMAL')
opcao = int(input('Sua opção: '))

if opcao == 1:
    numConvertido = bin(num)
    print(f'{num} convertido para BINÁRIO é igual a {numConvertido[2:]}')
elif opcao == 2:
    numConvertido = oct(num)
    print(f'{num} convertido para OCTAL é igual a {numConvertido[2:]}')
elif opcao == 3:
    numConvertido = hex(num)
    print(f'{num} convertido para HEXADECIMAL é igual a {numConvertido[2:]}')
else:
    print('Opção indefinida.')

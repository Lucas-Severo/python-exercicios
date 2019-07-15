'''
Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.
'''

numerosExtenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
                  'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze',
                  'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    while True:
        numero = int(input('Digite um número entre 0 e 20: '))

        if 20 >= numero >= 0:
            print(f'Você digitou o número {numerosExtenso[numero]}\n')
            break

        print('Tente novamente.', end=' ')

    while True:
        continuar = str(input('Você quer continuar?[S/N] ')).strip().upper()[0]
        if continuar == 'S' or continuar == 'N':
            break

    if continuar == 'N':
        break

    print()

print('FIM!')

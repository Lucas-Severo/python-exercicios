from cores import Cores  # necessário o arquivo cores.py

'''
Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
'''

cor = Cores()

numero1 = int(input('Primeiro valor: '))
numero2 = int(input('Segundo valor: '))
numero3 = int(input('Terceiro valor: '))

if numero1 >= numero2 and numero1 >= numero3:
    maior = numero1
    if numero2 > numero3:
        menor = numero3
    else:
        menor = numero2
else:
    if numero2 > numero1 and numero2 > numero3:
        maior = numero2
        if numero1 > numero3:
            menor = numero3
        else:
            menor = numero1
    else:
        maior = numero3
        if numero1 > numero2:
            menor = numero2
        else:
            menor = numero1

print(f'O menor valor digitado foi {cor.font("vermelho")}{menor}{cor.limpar()}')
print(f'O maior valor digitado foi {cor.font("verde")}{maior}{cor.limpar()}')

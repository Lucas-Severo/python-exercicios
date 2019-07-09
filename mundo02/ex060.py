'''
Faça um programa que leia um número qualquer e mostre o seu fatorial.

Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120
'''

print('Digite um número para')
num = int(input('Calcular seu Fatorial: '))
numero = num  # usar no for
fatorial = 1

# usando while
print(f'Calculando {num}! =', end=' ')
while num > 0:
    if num > 1:
        print(f'{num} x', end=' ')
    else:
        print(f'{num} =', end=' ')
    fatorial = fatorial * num
    num -= 1

print(fatorial)

# usando for

fatorial = 1
print(f'Calculando {numero}! =', end=' ')

for num in range(numero, 0, -1):
    if num > 1:
        print(f'{num} x', end=' ')
    else:
        print(f'{num} =', end=' ')
    fatorial *= num

print(fatorial)

'''
Faça um programa que leia uma frase pelo teclado
- e mostre quantas vezes aparece a letra "A",
- em que posição ela aparece a primeira vez
- e em que posição ela aparece a última vez.
'''

frase = str(input('Digite uma frase: ')).upper().strip()
contA = frase.count('A')
primeira = frase.find('A') + 1
ultima = frase.rfind('A') + 1

print('A letra A aparece {} vezes na frase.'.format(contA))
print('A primeira letra A apareceu na posição {}'.format(primeira))
print('A última letra A apareceu na posição {}'.format(ultima))

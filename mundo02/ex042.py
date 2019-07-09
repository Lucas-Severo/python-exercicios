'''
Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
- EQUILÁTERO: todos os lados iguais
- ISÓSCELES: dois lados iguais, um diferente
- ESCALENO: todos os lados diferentes
'''

seg1 = float(input('Primeiro segmento: '))
seg2 = float(input('Segundo segmento: '))
seg3 = float(input('Terceiro segmento: '))

if seg1 + seg2 > seg3 and seg1 + seg3 > seg2 and seg2 + seg3 > seg1:
    print('Os segmentos acima PODEM FORMAR um triângulo', end=' ')
    if seg1 == seg2 == seg3:
        print('EQUILÁTERO')
    elif seg1 == seg2 and seg1 != seg3 or seg1 == seg3 and seg1 != seg2 or seg2 == seg3 and seg2 != seg1:
        print('ISÓSCELES')
    else:
        print('ESCALENO')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

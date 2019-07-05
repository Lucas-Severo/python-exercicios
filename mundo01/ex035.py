from cores import Cores  # necessário o arquivo cores.py

'''
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.
'''

cor = Cores()

print('-='*15)
print('Analisador de Triângulos')
print('-='*15)

segmento1 = float(input('Primeiro Segmento: '))
segmento2 = float(input('Segundo Segmento: '))
segmento3 = float(input('Terceiro Segmento: '))

soma1 = segmento1 + segmento2
soma2 = segmento1 + segmento3
soma3 = segmento2 + segmento3

if soma1 > segmento3 and soma2 > segmento2 and soma3 > segmento1:
    print(f'Os segmentos acima {cor.font("verde")}PODEM FORMAR{cor.limpar()} um triângulo!')
else:
    print(f'Os segmentos acima {cor.font("vermelho")}NÃO PODEM FORMAR{cor.limpar()} um triângulo!')

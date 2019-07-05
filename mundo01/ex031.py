from cores import Cores

'''
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km
e R$0,45 parta viagens mais longas.
'''

cor = Cores()

distancia = float(input('Qual é a distância da sua viagem? '))
print(f'Você está prestes a começar uma viagem de {cor.font("vermelho")}{distancia}Km{cor.limpar()}')

if distancia > 200:
    valor = distancia * 0.45
    print(f'E o preço da sua passagem será de {cor.font("azul")}R${valor:.2f}{cor.limpar()}')
else:
    valor = distancia * 0.50
    print(f'E o preço da sua passagem será de {cor.font("azul")}R${valor:.2f}{cor.limpar()}')

# definição do valor em uma linha
valor = distancia * 0.45 if distancia > 200 else distancia * 0.50
print('E o preço da sua passagem será de R${:.2f}'.format(valor))

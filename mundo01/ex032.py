from cores import Cores
import datetime

'''
Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
'''

cor = Cores()

mensagemPositiva = f'{cor.font("verde")} É BISSEXTO {cor.limpar()}'
mensagemNegativa = f'{cor.font("vermelho")} NÃO É BISSEXTO {cor.limpar()}'

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = datetime.datetime.now().year

if ano % 4 == 0:
    if ano % 100 == 0:
        if ano % 400 == 0:
            print(f'O ano {ano}{mensagemPositiva}')
        else:
            print(f'O ano {ano}{mensagemNegativa}')
    else:
        print(f'O ano {ano}{mensagemPositiva}')
else:
    print(f'O ano {ano}{mensagemNegativa}')

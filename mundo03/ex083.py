'''
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão passada está:

- com os parênteses abertos e fechados na ordem correta.
'''

expressao = str(input('Digite a expressão: '))
parentesesFechados = 0
parentesesAbertos = 0

posicaoFechados = []
posicaoAbertos = []

for indice, caracter in enumerate(expressao):
    if caracter == '(':
        parentesesAbertos += 1
        posicaoAbertos.append(indice)
    elif caracter == ')':
        parentesesFechados += 1
        posicaoFechados.append(indice)

for i in range(0, parentesesAbertos):
    if parentesesAbertos == parentesesFechados:
        # se o parenteses fechados vir antes dos abertos, a expressão já está errada
        if posicaoAbertos[i] > posicaoFechados[i]:
            print('Sua expressão está errada!')
            break

        if i == parentesesAbertos - 1:
            print('Sua expressão está válida!')
    else:
        print('Sua expressão está errada!')
        break

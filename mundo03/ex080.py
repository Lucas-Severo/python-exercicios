'''
Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.
'''

valores = []

for contador in range(0, 5):
    numero = int(input('Digite um valor: '))

    if contador == 0:
        valores.append(numero)
        print('Adicionado ao final da lista...')
    else:
        for indice, valor in enumerate(valores):
            if numero <= valores[indice]:
                valores.insert(indice, numero)
                print(f'Adicionado na posição {indice} da lista...')
                break

            # se o índice for igual ao tamanho, é porque o número digitado não foi menor que nenhum da lista
            # então ele vai para o final da lista
            if indice == len(valores)-1:
                valores.append(numero)
                print('Adiconado ao final da lista...')
                break

print('-='*25)
print(f'Os valores digitados em ordem foram {valores}')

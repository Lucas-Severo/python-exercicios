'''
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
'''

matriz = [[], [], []]
somaPares = 0
somaTerceiraColuna = 0
maiorValorSegundaLinha = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha].append(int(input(f'Digite um valor para [{linha}, {coluna}]: ')))

        if matriz[linha][coluna] % 2 == 0:
            somaPares += matriz[linha][coluna]

        if coluna == 2:  # se for a terceira coluna
            somaTerceiraColuna += matriz[linha][coluna]

        if linha == 1:  # se for a segunda linha
            if matriz[linha][coluna] > maiorValorSegundaLinha:
                maiorValorSegundaLinha = matriz[linha][coluna]


print('-='*30)

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos valores pares é {somaPares}.')
print(f'A soma dos valores da terceira coluna é {somaTerceiraColuna}.')
print(f'O maior valor da segunda linha é {maiorValorSegundaLinha}.')

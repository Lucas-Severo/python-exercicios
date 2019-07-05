'''
Faça um algoritmo que leia o salário de um funcionário e
mostre seu novo salário, com 15% de aumento.
'''

salario = float(input('Qual é o salário do Funcionário? R$'))
# 100% + 15% = 115% -> 1.15
salarioN = salario * (1 + 0.15)

print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salario, salarioN))

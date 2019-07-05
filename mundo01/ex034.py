from cores import Cores  # necessário o arquivo cores.py

'''
Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
- Para salários superiores a R$1250,00, calcule um aumento de 10%.
- Para os inferiores ou iguais, o aumento é de 15%.
'''

cor = Cores()

salario = float(input('Qual é o salário do funcionário? R$'))

if salario > 1250:
    salarioReajustado = salario * (1 + 0.10)
else:
    salarioReajustado = salario * (1 + 0.15)

print('Quem ganhava {}R${:.2f}{} passa a ganhar {}R${:.2f}{} agora.'.format(cor.font('azul'), salario, cor.limpar(),
                                                                            cor.font('verde'), salarioReajustado, cor.limpar()))

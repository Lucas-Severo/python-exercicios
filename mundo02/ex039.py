'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade.
- se ele ainda vai se alistar ao serviço militar,
- se é a hora exata de se alistar
- se já passou do tempo do alistamento.

Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

anoNascimento = int(input('Ano de nascimento: '))
anoAtual = date.today().year
idade = anoAtual - anoNascimento

sexo = str(input('Digite seu sexo(homem ou mulher): ')).upper()

print(f'Quem nasceu em {anoNascimento} tem {idade} anos em {anoAtual}')

if sexo == 'HOMEM':
    if idade < 18:
        faltam = 18 - idade
        print(f'Ainda faltam {faltam} ano(s) para o alistamento')
        print(f'Seu alistamento será em {anoAtual + faltam}')
    elif idade == 18:
        print(f'Você tem que se alistar IMEDIATAMENTE')
    else:
        passou = idade - 18
        print(f'Você já deveria ter se alistado há {passou} ano(s)')
        print(f'Seu alistamento foi em {anoAtual - passou}')
elif sexo == 'MULHER':
    print('Alistamento não obrigatório')
else:
    print('opção indefinida')

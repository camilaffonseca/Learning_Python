# coding: utf-8

'''
Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar,
se é a hora exata de se alistar ou se já passou do tempo do alistamento.
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
'''

from datetime import date

def dif(idade) -> int:
    if idade < 18:
        return 18 - idade
    else:
        return idade - 18

ano_nascimento = int(input('Qual o ano do seu nascimento? \n> '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

print(f'Você tem {idade} anos.')

if idade > 18:
    print(f'Seu alistamento foi há {dif(idade)} ano(s),'
          f' em {ano_atual - dif(idade)}.')
elif idade < 18:
    print(f'Seu alistamento será daqui a {dif(idade)} ano(s),'
          f' em {ano_atual + dif(idade)}.')
else:
    print('Aliste-se imediatamente!')

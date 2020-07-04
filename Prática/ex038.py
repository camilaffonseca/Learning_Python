# coding: utf-8

'''
A Confederação Nacional de Natação precisa de um programa que leia o ano
de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
– Até 9 anos: MIRIM
– Até 14 anos: INFANTIL
– Até 19 anos: JÚNIOR
– Até 25 anos: SÊNIOR
– Acima de 25 anos: MASTER
'''

from datetime import date

nascimento = int(input('Qual seu ano de nascimento? '))
idade = date.today().year - nascimento

if idade < 9:
    categoria = 'Mirim'
elif idade > 9 and idade < 14:
    categoria = 'Infantil'
elif idade > 14 and idade < 19:
    categoria = 'Júnior'
elif idade > 19 and idade < 25:
    categoria = 'Sênior'
else:
    categoria = 'Master'

print(f'Nascido em {nascimento}'
      f'\n{idade} anos'
      f'\nCategoria {categoria}')

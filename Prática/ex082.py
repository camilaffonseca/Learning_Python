# coding: utf-8

'''
Crie um programa que leia nome, ano de nascimento e carteira de trabalho e
cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule
e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
'''

from datetime import datetime

dados = dict()

dados['Nome'] = input('Nome: ')
dados['Idade'] = datetime.now().year - int(input('Ano de nascimento: '))
dados['CTPS'] = int(input('CTPS: [0 - Não tem] > '))

if dados['CTPS'] != 0:
    dados['Contratação'] = int(input('Ano de contratação: '))
    dados['Salário'] = float(input('Salário: '))
    dados['Aposentadoria'] = dados['Idade'] + (35 - (datetime.now().year - dados['Contratação']))

print('=' * 30)

for k, v in dados.items():
    print(f'{k}: {v}')

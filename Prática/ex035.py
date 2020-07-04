# coding: utf-8

'''
Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. Pergunte o valor da casa, o salário do comprador e em
quantos anos ele vai pagar. A prestação mensal não pode exceder 30%
do salário ou então o empréstimo será negado.
'''


casa = float(input('Valor da casa: \n> R$ ').replace(',', '.'))
salario = float(input('Salário do comprador: \n> R$ ').replace(',', '.'))
tempo = int(input('Quantos anos de financiamento? \n> '))

prestação = casa / (tempo * 12)
porcentagem_salario = salario * 30 / 100

if prestação <= (porcentagem_salario - 200):
    print('Empréstimo aprovado!')
elif (prestação > (porcentagem_salario - 200)
        and prestação <= porcentagem_salario):
    print('Cuidado! Prestação mensal muito alta.'
          '\nEmpréstimo aprovado!')
else:
    print('Empréstimo negado!\nO valor mensal '
          'a pagar excede 30% do seu salário.')

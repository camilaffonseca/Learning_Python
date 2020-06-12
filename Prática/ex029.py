# coding: utf-8

'''
Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar
80km/h, mostre uma mensagem dizendo q ele foi multado.
A multa vai custar 7 reais por cada km acima do limite.
'''

velocidade = int(input('Qual a velocidade atual do carro em Km/h? '))

if velocidade > 80:
    print(f'Multado! Você excedeu o limite permitido de 80 Km/h \
    \nDeverá pagar uma multa de {(velocidade - 80) * 7} reais.')


print('Tenha um bom dia! Dirija com cuidado!')

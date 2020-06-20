# coding: utf-8

'''
Desenvolva um programa que pergunta a distância de uma viagem em Km.
Calcule o preço da passagem cobrando R$0,50 por km para viagens até 200km
e R$0,45 para viagens mais longas
'''


distancia = float(input('Qual a distância da sua viagem em km? '))

preço = distancia * 0.5 if distancia <= 200 else distancia * 0.45

print(f'A sua passagem custará {preço :.2f}')

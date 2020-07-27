# coding: utf-8

'''
Escreva um programa que 'pense' em um número para que o usuário adivinhe,
mostrando uma mensagem personalizada conforme acerto ou erro do usuário
'''


from random import randint

numero = randint(1, 5)

numero2 = int(input('Adivinhe em que número eu estou pensando :) \n> '))

if numero == numero2:
    print('Vc acertou ^^')
else:
    print(f'Infelizmente vc errou :( \nEu estava pensando em {numero}')

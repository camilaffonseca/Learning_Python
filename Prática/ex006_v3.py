# coding: utf-8

'''
Faça um programa que mostre a tabuada de vários números, um de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido quando
o número solicitado for 0.
'''

número = None

while True:

    print('\n- Tabuada -')
    número = int(input('\nNúmero: '))
    
    if número == 0:
        break

    for c in range(1, 11):
        print(f'{número} x {c:2} = {número * c}')
        c += 1

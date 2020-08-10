# coding: utf-8

print('Cálculo do Fatorial\n')

numero = int(input('Número: '))

fatorial = 1

print(f'{numero}! = ', end='')

while numero > 0:
    
    print(f'{numero}', end='')
    print(' x ' if numero > 1 else f' = {fatorial}', end='')

    fatorial *= numero
    numero -= 1

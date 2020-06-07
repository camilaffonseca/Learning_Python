# coding: utf-8

# Cálculo da hipotenusa

from math import hypot

oposto = float(input('Qual a medida do cateto oposto? '))
adjacente = float(input('Qual a medida do cateto adjacente? '))

hipotenusa = hypot(oposto, adjacente)

print(f'O valor da hipotenusa é {hipotenusa:.2f}')

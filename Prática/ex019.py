# coding: utf-8

# Cálculo de Seno, Cosseno e Tangente

import math

angulo = float(input('Digite o valor do ângulo: '))
angulo = math.radians(angulo)

sen = math.sin(angulo)
cos = math.cos(angulo)
tang = math.tan(angulo)

print(f'O ângulo possui seno de {sen:.2f} \nCosseno de {cos:.2f} e \
\nTangente de {tang:.2f}')

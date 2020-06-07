# coding: utf-8

# Cálculo de Seno, Cosseno e Tangente


from math import radians, sin, cos, tan

angulo = float(input('Digite o valor do ângulo: '))
angulo = radians(angulo)

sen = sin(angulo)
cos = cos(angulo)
tang = tan(angulo)

print(f'O ângulo possui seno de {sen:.2f} \nCosseno de {cos:.2f} e \
\nTangente de {tang:.2f}')

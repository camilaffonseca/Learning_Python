# coding: utf-8

pesos = []
for p in range(1, 6):
    pesos.append(float(input(f'Peso {p}: ')))

pesos = sorted(pesos)

print(f'O menor peso foi {pesos[0]} e o maior foi {pesos[-1]}')

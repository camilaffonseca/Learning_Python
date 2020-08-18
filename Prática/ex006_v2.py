# coding: utf-8

# upgrade ex006

num = int(input('Digite um número para ver sua tabuada: '))

for c in range(1, 11):
    print(f'{num} X {c :2} = {num * c}')

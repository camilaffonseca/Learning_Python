# coding: utf-8

print('- Sequência de Fibonacci -')

quantidade_de_termos = int(input('Quantos termos você quer mostrar? '))

termo1 = 0
termo2 = 1
c = 2

if quantidade_de_termos == 1:
    print(termo1)
elif quantidade_de_termos == 2:
    print(f'{termo1} - {termo2}')
else:
    print(f'{termo1} - {termo2}', end='')
    while c < quantidade_de_termos:
        soma = termo1 + termo2
        print(f' - {soma}', end='')
        termo1 = termo2
        termo2 = soma
        c += 1

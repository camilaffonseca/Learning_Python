'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No
início, pergunte ao usuário qual será o valor a ser sacado (número inteiro)
e o programa vai informar quantas cédulas de cada valor serão entregues.
OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
'''

while True:
    try:
        valor = int(input('Qual o valor do saque? R$'))
        break

    except Exception:
        print('Por favor, digite um valor inteiro!')

print(f'O valor será entregue em...')

cédula = 50
total_de_cédulas = 0

while True:

    if valor >= cédula:
        valor -= cédula
        total_de_cédulas += 1

    else:

        if total_de_cédulas > 0:
            print(f'{total_de_cédulas} cédulas de R${cédula}')

        total_de_cédulas = 0

        if valor >= 20:
            cédula = 20
        elif valor >=10:
            cédula = 10
        elif valor < 10:
            cédula = 1
        
        if valor == 0:
            break

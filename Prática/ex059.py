# coding: utf-8

'''
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, o programa deverá perguntar se o
usuário quer ou não continuar. No final, mostre:
A) quantas pessoas tem mais de 18 anos.
B) quantos homens foram cadastrados.
C) quantas mulheres tem menos de 20 anos.
'''

pessoas_18 = 0
homens = 0
mulheres_20 = 0

while True:
    
    while True:
        try:
            idade = int(input('Idade: '))
            break
        except Exception:
            print('Resposta Inválida! \nDigite um número inteiro...')
    
    while True:
        sexo = input('Sexo: ').upper()[0]
        
        if sexo in 'FM':
            break
        else:
            print('Resposta Inválida! \nDigite MASCULINO ou FEMININO...')

    if idade >= 18:
        pessoas_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulheres_20 += 1

    opção = ' '

    while True:
        opção = input('Continuar? ').upper()[0]
        if opção in 'NS':
            break
        else:
            print('Resposta inválida! \nResponda com SIM ou NÃO...')

    if opção == 'N':
        break

print(f'\nPessoas acima de 18 anos: {pessoas_18}'
      f'\nHomens cadastrados: {homens}'
      f'\nMulheres abaixo de 20 anos: {mulheres_20}')

# coding: utf-8

'''
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e
qual foi o maior e o menor valores lidos. O programa deve perguntar
ao usuário se ele quer ou não continuar a digitar valores.
'''



soma = c = 0
maior = menor = 0
opção = 'S'

while opção[:1] == 'S':
    
    valor = float(input('Valor: '))
    
    soma += valor
    c += 1

    if c == 1:
        maior = menor = valor
    else:
        if valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor

    opção = input('Continuar? ').upper()
 

print(f'\nMédia: {soma / c}'
      f'\nMaior: {maior}'
      f'\nMenor: {menor}')

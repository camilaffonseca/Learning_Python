# coding: utf-8

'''
Crie um programa onde o usuário digite uma expressão qualquer que use
parênteses. Seu aplicativo deverá analisar se a expressão passada está
com os parênteses abertos e fechados na ordem correta
'''

expressão = input('Digite a expressão: ')
parenteses = []

for item in expressão:
    if item == '(':
        parenteses.append(item)
    elif item == ')':
        if parenteses:
            parenteses.pop()
        else:
            parenteses.append(item)
            break

if parenteses:
    print('Expressão inválida, os parênteses estão mal colocados.')
else:
    print('Expressão válida!')

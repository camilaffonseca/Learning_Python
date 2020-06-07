# coding: utf-8

# Sorteando item na lista


from random import choice

aluno1 = input('Primeiro aluno: ')
aluno2 = input('Segundo aluno: ')
aluno3 = input('Terceiro aluno: ')
aluno4 = input('Quarto aluno: ')
aluno5 = input('Quinto aluno: ')

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
sorteado = choice(lista)

print(f'O aluno sorteado foi {sorteado}')

# coding: utf-8

'''
Faça um programa que leia nome e média de um aluno, 
guardando também a situação em um dicionário.
No final, mostre o conteúdo da estrutura na tela.
'''


aluno = {}

aluno['nome'] = input('Nome do aluno: ')

aluno['notas'] = []


contagem = 0
while True:
    contagem += 1

    if contagem > 1:
        print('[Digite um número negativo p/ parar]')

    nota = float(input(f'Nota {contagem}: '))

    if nota < 0:
        break

    aluno['notas'].append(nota)

soma = 0
for nota in aluno['notas']:
    soma += nota

aluno['média'] = soma / len(aluno['notas'])

if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

print(f'Al {aluno["nome"]} com média {aluno["média"]:2f} está {aluno["situação"]}')

while True:
    opção_mostrar_notas = input('Mostrar notas do aluno? ')[0].upper()
    if opção_mostrar_notas in 'SN':
        break

if opção_mostrar_notas == 'S':
    print('\n'.join(map(str, aluno['notas'])))

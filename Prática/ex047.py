# coding: utf-8

'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre: a média de idade do grupo, qual é o nome
do homem mais velho e quantas mulheres têm menos de 20 anos.
'''

soma_idades = 0
idade_homem_mais_velho = 0
nome_homem_mais_velho = ''
cont_mulheres = 0
for p in range(1, 5):
    
    print(f'Pessoa {p}')
    
    nome = input('Nome: ')
    idade = int(input('Idade: '))
    sexo = input('Sexo (M/F): ').upper()
    
    soma_idades += idade
    
    if sexo == 'M':
        if idade > idade_homem_mais_velho:
            idade_homem_mais_velho = idade
            nome_homem_mais_velho = nome

    if sexo == 'F':
        if idade < 20:
            cont_mulheres += 1

print(f'A média de idades é {soma_idades/4}'
      f'\nO homem mais velho é {nome_homem_mais_velho}, com {idade_homem_mais_velho} anos'
      f'\nMulheres com menos de 20 anos: {cont_mulheres}')

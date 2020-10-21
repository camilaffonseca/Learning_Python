# coding: utf-8

'''
Crie um programa que gerencie o aproveitamento de um jogador de futebol.
O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois
vai ler a quantidade de gols feitos em cada partida. No final, tudo isso
será guardado em um dicionário, incluindo o total de gols feitos 
no campeonato.
'''


jogador = {}

jogador['nome'] = input('Nome: ')
jogador['partidas'] = int(input('Jogou quantas partidas? '))


gols_partida = []

for partida in range(0, jogador['partidas']):
    gols_partida.append(int(input(f'Gols na partida {partida + 1}: ')))

jogador['gols_partida'] = gols_partida
jogador['total_gols'] = sum(gols_partida)


print(f'\nNome: {jogador["nome"].title()}'
      f'\nTotal de gols: {jogador["total_gols"]}')

for partida, gols_partida in enumerate(jogador['gols_partida']):
    print(f'Partida {partida + 1}: {gols_partida} gols')

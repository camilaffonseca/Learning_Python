# coding: utf-8

'''
Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo
um sistema de visualização de detalhes do aproveitamento de cada jogador.
'''


jogadores = []

while True:
    jogador = {}

    jogador['nome'] = input('Nome: ')
    jogador['partidas'] = int(input('Jogou quantas partidas? '))


    gols_partida = []

    for partida in range(0, jogador['partidas']):
        gols_partida.append(int(input(f'Gols na partida {partida + 1}: ')))

    jogador['gols_partida'] = gols_partida
    jogador['total_gols'] = sum(gols_partida)
    
    jogadores.append(jogador)

    opção_continuar = input('Continuar? ').upper()[0]
    
    if opção_continuar == 'N':
        break

print('Nome'.center(20),
      'Gols por partida'.center(20),
      'Total de gols'.center(10),
      sep=' | ')

for jogador in jogadores:
    print(
        f'{jogador["nome"].title()}'.center(20),
        f'{", ".join(map(str, jogador["gols_partida"]))}'.center(20),
        f'{jogador["total_gols"]}'.center(10),
        sep=' | '
    )

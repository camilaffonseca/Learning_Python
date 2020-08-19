# coding: utf-8

'''
Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times.
b) Os últimos 4 colocados.
c) Times em ordem alfabética.
d) Em que posição está o time do Grêmio.
'''

times_brasileirão = ('Atlético-MG', 'Vasco da Gama', 'Internacional', 'Bahia',
                     'Atlético-PR', 'Grêmio', 'Atlético-GO', 'Santos',
                     'Fluminense', 'Sport Recife', 'São Paulo', 'Flamengo',
                     'Palmeiras', 'Botafogo', 'Bragantino-SP', 'Corinthians',
                     'Goiás', 'Ceará SC', 'Fortaleza', 'Coritiba')

print('\n', '=' * 36,
      '\n20 primeiros colocados do Brasileirão:')

for time in times_brasileirão:
      print(time)

print('=' * 30,
      '\nPrimeiros 5 times:')

for time in times_brasileirão[0: 5]:
      print(time)

print('=' * 30,
      '\nÚltimos 4 times:')

for time in times_brasileirão[-4:]:
      print(time)

print('=' * 30,
      f'\nPosição do Grêmio: {times_brasileirão.index("Grêmio") + 1}')

print('=' * 30,
      '\nTimes em ordem alfabética:')

for time in sorted(times_brasileirão):
      print(time)

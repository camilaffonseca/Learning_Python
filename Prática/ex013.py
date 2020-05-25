# coding: utf-8

'''
Faça um programa que pergunte em que turno você estuda.
Peça para digitar M-matutino ou V-Vespertino ou N- Noturno.
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!"
ou "Valor Inválido!", conforme o caso.
'''

nome = input('Qual é o seu nome? ')
turno = input('Em que turno você estuda? \nDigite: \nM - Matutino \
\nV - Vespertino \nN - Noturno \n>')

if turno == 'M' or turno == 'm':
	print(f'Bom dia, {nome}')
elif turno == 'V' or turno == 'v':
	print(f'Boa tarde, {nome}')
elif turno == 'N' or turno == 'n':
	print(f'Boa noite, {nome}')
else:
	print('Valor inválido')

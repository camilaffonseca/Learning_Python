# coding: utf-8

# Faça um Programa que leia dois números e mostre o menor deles.


numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))

if numero1 < numero2:
	print(f'{numero1} é menor que {numero2}.')
elif numero1 > numero2:
	print(f'{numero2} é menor que {numero1}.')
elif numero1 == numero2:
	print(f'{numero1} e {numero2} são iguais.')

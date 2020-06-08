# coding: utf-8

# Faça um programa que leia o nemo de uma cidade e verifique se ela começa com a palavra Santo


cidade = str(input('Digite o nome da cidade: ')).strip()

if cidade[:5].title() == 'Santo':
    print('O nome da cidade que vc digitou começa com a palavra Santo')
else:
    print('O nome da cidade que vc digitou não começa com a palavra Santo')

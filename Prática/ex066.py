# coding: utf-8

'''
Crie um programa que tenha uma tupla única com nomes de produtos
e seus respectivos preços, na sequência. No final, mostre uma
listagem de preços, organizando os dados em forma tabular.
'''

produtos = ()
opção_continuar = ' '
preço_produto = None

while opção_continuar != 'n':
    nome_produto = input('Nome do produto: ')
    
    while True:
        try:
            preço_produto = float(input('Preço do produto: '))
            break
        except Exception:
            print('Valor inválido!')
        
    produtos += nome_produto, preço_produto
    
    while True:
        opção_continuar = input('Continuar? ').lower()[0]
        if opção_continuar in 'sn':
            break
        else:
            print('Resposta inválida!')

for ítem in range(0, len(produtos)):
    if ítem % 2 == 0:
        print(f'{produtos[ítem].upper():.<30}', end='')
    else:
        print(f'R$ {produtos[ítem]:.2f}')

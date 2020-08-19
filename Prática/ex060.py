# coding: utf-8

'''
Crie um programa que leia o nome e o preço de vários produtos. O programa
deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra.
B) quantos produtos custam mais de R$1000.
C) qual é o nome do produto mais barato.
'''

total_da_compra = contagem_produtos_1000 = contagem_produtos = 0
preço_produto_mais_barato = nome_produto_mais_barato = None

while True:

    nome_produto = input('Nome do produto: ')
    while True:
        try:
            preço_produto = float(input('Valor do produto: R$').replace(',', '.'))
            break
        except Exception:
            print('Valor inválido, digite novamente!')

    total_da_compra += preço_produto
    contagem_produtos += 1

    if preço_produto > 1000.00:
        contagem_produtos_1000 += 1

    if contagem_produtos == 1 or preço_produto < preço_produto_mais_barato:
        preço_produto_mais_barato = preço_produto
        nome_produto_mais_barato = nome_produto

    opção = ' '
    while True:
        opção = input('Registrar mais um produto? ').lower()[0]
        if opção in 'sn':
            break
        else:
            print('Resposta inválida! Digite SIM ou NÃO...')

    if opção == 'n':
        break

print(f'\nProdutos registrados: {contagem_produtos}'
      f'\nProdutos acima de R$1000,00: {contagem_produtos_1000}'
      f'\nTotal da compra: R${total_da_compra:.2f}'
      f'\nProduto mais barato: {nome_produto_mais_barato} '
      f'(R${preço_produto_mais_barato:.2f})')

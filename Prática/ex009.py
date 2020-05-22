# coding: utf-8


preço = float(input('Digite o preço do produto em reais: '))

desconto = preço - (preço * 5 / 100)

print(f'Com 5 porcento de desconto o produto fica no valor de \
R${desconto:.2f}')

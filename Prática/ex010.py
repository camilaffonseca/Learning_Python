# coding: utf-8

# Reajuste salarial


salario = float(input('Qual o salário do funcionário em reais? '))
aumento = float(input('Qual a porcentagem do aumento salarial? '))

salario2 = salario + (salario * aumento / 100)

print(f'O salário de R${salario:.2f} com aumento de {aumento} porcento ficaria \
no valor de R${salario2:.2f}')

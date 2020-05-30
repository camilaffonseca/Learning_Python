# coding: utf-8

'''
Faça um programa que recebe o salário e o reajuste segundo o seguinte critério,
baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
''' 

salario = (input('Digite o valor do seu salário: R$'))
salario = float(salario.replace(',', '.'))

if salario <= 280:
	percentual = 20
elif salario > 280 and salario <= 700:
	percentual = 15
elif salario > 700 and salario <= 1500:
	percentual = 10
elif salario > 1500:
	percentual = 5

aumento = salario * percentual / 100
salario2 = salario + aumento

print(f'''
Salário inicial: R${salario}
Percentual de aumento aplicado: {percentual}%
Valor do aumento: R${aumento:.2f}
Valor do salário após o aumento: R${salario2}
''')

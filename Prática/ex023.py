# coding: utf-8

# Separação de dígitos de um número inteiro


numero = input('Digite um número: ').zfill(4)

unidade = numero[3]
dezena = numero[2]
centena = numero[1]
milhar = numero[0]

print(f'''Análise do número {numero.lstrip('0')}
Unidade: {unidade}
Dezena: {dezena}
Centena: {centena}
Milhar: {milhar}
''')

# coding: utf-8

# Análise de textos


nome = str(input('Digite seu nome completo: ')).strip()

maiusculo = nome.upper()
minusculo = nome.lower()
nome_dividido = nome.split()
quantidade_letras = len(''.join(nome_dividido))
primeiro_nome = nome_dividido[0]

print(f'''
Seu nome com todas as letras maiúsculas é: {maiusculo}
Seu nome com todas as letras minúsculas é: {minusculo}
Seu nome tem {quantidade_letras} letras no total
Seu primeiro nome é {primeiro_nome} e tem {len(primeiro_nome)} letras
''')

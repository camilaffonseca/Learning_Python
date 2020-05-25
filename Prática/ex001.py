# coding: utf-8

# Dissecando uma variável


variavel = input('Digite algo: ')

print(f'''
O tipo primitivo de '{variavel}' é {type(variavel)}
Tem somente espaços? {variavel.isspace()}
É numérico? {variavel.isnumeric()}
É alfabético? {variavel.isalpha()}
É alfanumérico? {variavel.isalnum()}
Está em maiúsculas? {variavel.isupper()}
Está em minúsculas? {variavel.islower()}
Está capitalizado? {variavel.istitle()}
''')

# coding: utf-8

# Dissecando uma variável


x = input('Digite algo: ')
if x.isspace() == False:
    x = x.strip()

print(f'''
O tipo primitivo de '{x}' é {type(x)}
Tem somente espaços? {x.isspace()}
É numérico? {x.isnumeric()}
É alfabético? {x.isalpha()}
É alfanumérico? {x.isalnum()}
Está em maiúsculas? {x.isupper()}
Está em minúsculas? {x.islower()}
Está capitalizado? {x.istitle()}
''')

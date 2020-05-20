a = input('Digite algo: ')

print(f'''
O tipo primitivo de '{a}' é {type(a)}
Tem somente espaços? {a.isspace()}
É numérico? {a.isnumeric()}
É alfabético? {a.isalpha()}
É alfanumérico? {a.isalnum()}
Está em maiúsculas? {a.isupper()}
Está em minúsculas? {a.islower()}
Está capitalizado? {a.istitle()}
''')
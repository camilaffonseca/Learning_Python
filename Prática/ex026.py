# coding: utf-8

# Primeira e última ocorrência de uma string


frase = input('Digite uma frase: ').lower().strip()
quantidade = frase.count('a')
primeira = frase.find('a') + 1
ultima = frase.rfind('a') + 1

print(f'''
A frase repete {quantidade} vezes a letra 'A'
A primeira vez que a letra 'A' aparece na frase é na posição {primeira}
E a ultima vez que a letra 'A' aparece é na posição {ultima}
''')

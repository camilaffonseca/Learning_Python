# coding: utf-8

print('| Detector de Palíndromos | \n')

frase = str(input('Digite a frase: \n> ')).upper()
frase_op = frase[::-1]

print(f'{frase} ao contrário é {frase_op}')

if frase == frase_op:
    print(f'{frase} é um palíndromo')
else:
    print(f'{frase} não é um palíndromo')

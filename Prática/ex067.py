# coding: utf-8

'''
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
'''


opção_continuar = ' '
vogais = ['a', 'e', 'i', 'o', 'u']

while True:
    palavra = input('Palavra: ')
    print(f'Vogais da palavra {palavra}: ', end='')
    for letra in palavra:
        if letra.lower() in vogais:
            print(letra, ' ', end='')
    while True:
        opção_continuar = input('\nContinuar? ').lower()[0]
        if opção_continuar in 'sn':
            break
        else:
            print('Resposta inválida!')
    if opção_continuar == 'n':
        break

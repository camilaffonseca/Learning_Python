# coding: utf-8

'''
Crie um programa que leia nome e duas notas de vários alunos e
guarde tudo em uma lista composta. No final, mostre um boletim
contendo a média de cada um e permita que o usuário possa
mostrar as notas de cada aluno individualmente.
'''


lista_alunos = []
c = 0

while True:
    c += 1

    aluno_temp = []

    print(f'ALUNO {c}')

    aluno_temp.append(input('Nome: '))
    
    notas_temp = []

    while True:
        while True:
            try:
                notas_temp.append(float(input('Nota: ')))
                break
            except Exception:
                print('Valor inválido. '
                      'Tente novamente!')

        while True:
            opção_add_notas = input('Mais uma? ').upper()[0]

            if opção_add_notas in 'SN':
                break
            else:
                print('Responda com SIM ou NÃO :)')

        if opção_add_notas == 'N':
            break

    aluno_temp.append(notas_temp)

    lista_alunos.append(aluno_temp)

    while True:
        opção_add_aluno = input('Adicionar outro aluno? ').upper()[0]

        if opção_add_aluno in 'SN':
            break
        else:
            print('Responda com SIM ou NÃO :)')

    if opção_add_aluno == 'N':
        break

for aluno in lista_alunos:
    soma = 0

    for nota in aluno[1]:
        soma += nota

    média = soma / len(aluno[1])

    aluno.append(média)

print('BOLETIM'.center(46, '-'))

for indice, aluno in enumerate(lista_alunos):
    print(f'Nº {indice + 1 :^6}',
          f'Al {aluno[0] :^15}',
          f'Média {aluno[-1] :^8}',
          sep=' | ')

while True:
    opção_aluno = input('\nMostrar notas de qual aluno? [0 p/ finalizar] > ')
    
    if opção_aluno == '0':
        break

    if opção_aluno.isnumeric() == False:
        for indice, aluno in enumerate(lista_alunos):
            if opção_aluno.upper() == aluno[0].upper():
                opção_aluno = indice + 1
                break

    try:
        print(f'Al {lista_alunos[int(opção_aluno) - 1][0]} | ',
            ' | '.join(map(str, lista_alunos[int(opção_aluno) - 1][1])))
    except Exception:
        print(f'O aluno {opção_aluno} não foi encontrado na lista.')

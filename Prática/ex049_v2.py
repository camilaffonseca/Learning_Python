# coding: utf-8


from unidecode import unidecode


def realocar_espaços(frase):
    frase_separada = unidecode(frase).split(' ')

    lista_de_tamanhos = []

    for palavra in frase_separada:
        lista_de_tamanhos.append(len(palavra))

    frase_sem_espaços_invertida = unidecode(
        frase[::-1].replace(' ', '')
    )

    lista_caracteres_invertidos = []

    for índice in range(len(frase_sem_espaços_invertida)):
        lista_caracteres_invertidos.append(frase_sem_espaços_invertida[índice])

    indice_anterior = 0
    lista_separada_por_palavras_invertidas = []

    for tamanho in lista_de_tamanhos:
        lista_separada_por_palavras_invertidas.append(
            lista_caracteres_invertidos[
                indice_anterior:indice_anterior + tamanho
            ]
        )

        indice_anterior = tamanho + indice_anterior

    lista_de_apalvras_processadas = []

    for índice_palavra in range(len(lista_separada_por_palavras_invertidas)):

        lista_da_palavra = lista_separada_por_palavras_invertidas[índice_palavra]

        palavra = ''

        for índice_letra_palavra in range(len(lista_da_palavra)):
            palavra += lista_da_palavra[índice_letra_palavra]

        lista_de_apalvras_processadas.append(palavra)

    frase_ao_contrário = ''

    for índice_palavra in range(len(lista_de_apalvras_processadas)):

        frase_ao_contrário += lista_de_apalvras_processadas[índice_palavra] + ' '
    
    frase_ao_contrário = frase_ao_contrário[0:-1]
    
    return frase_ao_contrário


print('| Detector de Palíndromos | \n')

frase = input('Digite a frase: \n> ').upper()

frase_op = realocar_espaços(frase)

print(f'\n{frase}\n\nAo contrário é:\n\n{frase_op}')

if unidecode(frase.replace(' ', '')) == unidecode(frase_op.replace(' ', '')):
    print(f'\n{frase} é um palíndromo')
else:
    print(f'\n{frase} não é um palíndromo')

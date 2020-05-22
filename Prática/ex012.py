# coding utf-8


distancia = float(input('Distância percorrida em Km: '))
dias = int(input('Quantos dias alugados? '))

preço = (0.15 * distancia) + (60 * dias)

print(f'O valor total a pagar por {dias} dias e {distancia}Km é de R${preço}')

# coding: utf-8

# Classificação dos triângulos

def ident_triangulos(segmento1, segmento2, segmento3) -> str:
    '''Identifica o tipo de triângulo com base nos seus lados.
    
    Com base na relação dos seus lados, retorna EQUILÁTERO,
    ESCALENO ou ISÓSCELES.
    '''

    if seg1 == seg2 and seg1 == seg3:
        return 'EQUILÁTERO'
    elif seg1 != seg2 and seg1 != seg3 and seg2 != seg3:
        return 'ESCALENO'
    else:
        return 'ISÓSCELES'

seg1 = float(input('Primeira reta: '))
seg2 = float(input('Segunda reta: '))
seg3 = float(input('Terceira reta: '))

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Os segmentos acima podem formar um triângulo '
          f'{ident_triangulos(seg1, seg2, seg3)}')
else:
    print('Os segmentos acima não podem formar um triângulo')

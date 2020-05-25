# coding: utf-8

# Cálculo da quantidade necessária de tinta para pintar uma parede


altura = float(input('Altura da parede em metros: '))
largura = float(input('Largura da parede em metros: '))

area = altura*largura

print(f'A área da parede é {area}m^2, portanto serão necessários \
{area / 2}L de tinta')

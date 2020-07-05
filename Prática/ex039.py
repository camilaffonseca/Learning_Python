# coding: utf-8

'''
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu Índice de Massa Corporal (IMC) e mostre seu status,
de acordo com a tabela abaixo:
– IMC abaixo de 18,5: Abaixo do Peso
– Entre 18,5 e 25: Peso Ideal
– 25 até 30: Sobrepeso
– 30 até 40: Obesidade
– Acima de 40: Obesidade Mórbida
'''

def imc_status(imc) -> str:
    '''Identifica o status corporal conforme IMC.
    
    Com base no valor do IMC, retorna Abaixo do Peso, Peso Ideal,
    Sobrepeso, Obesidade ou Obesidade Mórbida.
    '''
    if imc < 18.5:
        return 'Abaixo do Peso'
    elif imc < 25 and imc >= 18.5:
        return 'Peso Ideal'
    elif imc < 30 and imc >= 25:
        return 'Sobrepeso'
    elif imc < 40 and imc >= 30:
        return 'Obesidade'
    else:
        return 'Obesidade Mórbida'

peso = float(input('Seu peso em Kg: \n> ').replace(',', '.'))
altura = float(input('Sua altura em metros: \n> ').replace(',', '.'))

imc = peso / (altura**2)

print(f'IMC: \n> {imc:.2f} \nStatus: \n> {imc_status(imc)}')

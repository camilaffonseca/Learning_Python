# coding: utf-8
# Estruturas condicionais


# mensagem = input('Você > ')
# while mensagem != 'sair':
#     if mensagem == 'ola':
#         print('Robô - Olá também!')
#     elif mensagem == 'bom dia':
#         print('Robô - Bom dia para você também!')
#     elif mensagem == 'tchau':
#         print('Robô - Que pena que vai embora :(\nTchau!')
#     else:
#         print('Robô - Não consigo entender o que você disse :/')
#     mensagem = input('Você > ')


# senha = '12345'
# senha_gerente = input('Digite a senha do sistema: ')
# if senha == senha_gerente:
#     salario = float(input('Qual o salário do funcionário em reais? '))
#     while True:
#         print('''
#         Selecione a opção do aumento correspondetnte:
#         1 - Aumento de 5%
#         2 - Aumento de 10%
#         ''')
#         opcao = input('Digite a opção > ')
#         if opcao == '1':
#             aumento = 5
#             salario2 = salario + (salario * 5 / 100)
#             print(f'O salário de R${salario:.2f} com aumento de {aumento} porcento ficaria \
# no valor de R${salario2:.2f}')
#             break
#         elif opcao == '2':
#             aumento = 10
#             salario2 = salario + (salario * 10 / 100)
#             print(f'O salário de R${salario:.2f} com aumento de {aumento} porcento ficaria \
# no valor de R${salario2:.2f}')
#             break
#         else:
#             print('Opção inválida!')
# else:
#     print('Senha incorreta! Saia daqui!')


'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''


# turno = input('Em que turno vc estuda?\nDigite:\nM-matutino\nV-vespertino\nN-noturno\n> ')

# if turno == 'M' or turno == 'm':
#     print('Bom dia!')
# elif turno == 'V' or turno == 'v':
#     print('Boa tarde!')
# elif turno == 'N' or turno == 'n':
#     print('Boa noite!')
# else:
#     print('Valor inválido!')

'''
Faça um Programa que leia dois números e mostre o menor deles.
'''

# numero1 = int(input('Digite o primeiro número: '))
# numero2 = int(input('Digite o segundo número: '))

# if numero1 < numero2:
#     print('O número 1 é o menor')
# elif numero2 < numero1:
#     print('O número 2 é o menor')
# elif numero2 == numero1:
#     print('Os dois números são iguais')


'''
Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:

- A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
- A mensagem "Reprovado", se a média for menor do que sete;
- A mensagem "Aprovado com Distinção", se a média for igual a dez.
'''


nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7 and media != 10:
    print(f'Aprovado com {media}')
elif media < 7:
    print(f'Reprovado com {media}')
elif media == 10:
    print('Aprovado com distinção')




'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contrataram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
- salários até R$ 280,00 (incluindo) : aumento de 20%
- salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
- salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
- salários de R$ 1500,00 em diante : aumento de 5% 
Após o aumento ser realizado, informe na tela:
- o salário antes do reajuste;
- o percentual de aumento aplicado;
- o valor do aumento;
- o novo salário, após o aumento.
'''
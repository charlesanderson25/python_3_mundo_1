#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

# Um ano é bissexto se for divisível por 4, mas não por 100, a menos que também seja divisível por 400.

import datetime

ano = int(input('Informe um ano que deseja analisar ou informe 0 para o ano atual:'))

if ano == 0:
    ano = datetime.date.today().year
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print('O ano de {} é bissexto '.format(ano))
else:
    print('O ano de {} não é bissexto!'.format(ano))


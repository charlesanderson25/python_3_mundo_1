#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Informe uma frase qualquer:'))
letraA = str(input('Informe a letra que deseja pesquisar:'))

maiusculas = str(frase.upper())

print('Estão MAIÚSCULAS?: {}'.format(maiusculas))

posicaoLetraA = maiusculas.find('A')

print('A primeira posição que a letra {}'.format(letraA), 'aparece é: {}'.format(posicaoLetraA))

posicaoFinalLetraA = maiusculas.rfind('A')

print('A ultima posição que a letra {}'.format(letraA), 'aparece é: {}'.format(posicaoFinalLetraA))
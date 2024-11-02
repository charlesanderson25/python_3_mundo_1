#Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

numeroInt = int(input('Informe um número inteiro:'))

if numeroInt % 2 == 0:
    print('O número {} é PAR!'.format(numeroInt))
else:
    print('O número {} é ÍMPAR!'.format(numeroInt))
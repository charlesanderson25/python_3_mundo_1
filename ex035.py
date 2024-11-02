#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

numero1 = int(input('Informe o primeiro número:'))
numero2 = int(input('Informe o segundo número:'))
numero3 = int(input('Informe o terceiro número:'))

if numero1 > numero2 and numero1 > numero3:
    print('O número {} é o maior!'.format(numero1))
if numero2 > numero1 and numero2 > numero3:
    print('O número {} é o maior'.format(numero2))
if numero3 > numero1 and numero3 > numero2:
    print('O número {} é o maior'.format(numero3))
if numero1 < numero2 and numero1 < numero3:
    print('O número {} é o menor'.format(numero1))
if numero2 < numero1 and numero2 < numero3:
    print('O número {} é o menor'.format(numero2))
if numero3 < numero1 and numero3 < numero2:
    print('O número {} é o menor'.format(numero3))
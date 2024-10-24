# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Informe uma frase qualquer:'))

fraseMinuscula = str(frase.lower())

print('Estão minúsculas? {}'.format(fraseMinuscula))

verificaLetraA = fraseMinuscula.find('a')

print(verificaLetraA)

divideFrase = str(fraseMinuscula.split())

print(divideFrase)

verificaLetraA1 = str(divideFrase.split([0]))

print(verificaLetraA1)
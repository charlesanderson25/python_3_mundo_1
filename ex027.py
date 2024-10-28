# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Informe uma frase qualquer:'))

contagemDoA = str(input('Informe a string que deseja verificar:'))

fraseMinuscula = str(frase.lower())

print('Estão minúsculas? {}'.format(fraseMinuscula))

verificaLetraA = fraseMinuscula.find('a')

print('A primeira vez que a letra _a_ aparece é na posição: {}'.format(verificaLetraA))

qtdRepeticao = str(fraseMinuscula.count(contagemDoA))

print('A quantidade de vezes que a string _a_ se repete é:{}'.format(qtdRepeticao))

verificaUltimaPosicao = fraseMinuscula.rfind('a')

print('A última vez que a letra _a_ aparece é na posição: {}'.format(verificaUltimaPosicao))


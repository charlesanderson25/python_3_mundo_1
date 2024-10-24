#Crie um programa que leia o nome de uma pessoa e diga se ela tem “SILVA” no nome.

nome = str(input('Informe seu nome:'))

nomeMaiusculo = str(nome.upper())

verificaNome = 'SILVA' in nomeMaiusculo

print('Existe SILVA no nome informado? {}'.format(verificaNome))
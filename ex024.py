#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

import random

numero = str(random.randint(1, 9999))

print(numero)

divideNumero = str(numero.split())

print(divideNumero)

delimiter = str('-'.join(divideNumero))

print(delimiter)

divideDelimiter = str(delimiter.split())

divideDelimiter1= " ".join(divideDelimiter)

print(divideDelimiter1.split())




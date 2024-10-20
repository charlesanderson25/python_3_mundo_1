#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import random
import math

num = random.uniform(0, 999.9)

print(num)

print('O número inteiro gerado é:', math.floor(num))




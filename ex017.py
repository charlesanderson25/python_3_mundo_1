#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

import random
import math

num = random.uniform(0, 999.9)

print('O número gerado pelo Random é:',num)

print('Sua porção inteira convertida pelo método Math é:', math.floor(num))




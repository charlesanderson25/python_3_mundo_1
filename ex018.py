#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento da hipotenusa.

catetoAdjacente = float(input('Informe o comprimento do cateto adjacente: '))
catetoOposto = float(input('Informe o comprimento do cateto oposto: '))

calculoCatetos = (catetoAdjacente ** 2) + (catetoOposto ** 2)

calculoHipotenusa = calculoCatetos ** (1/2)

print('O valor da hipotenusa é: {:.2f}'.format(calculoHipotenusa))

'''/////////////////////////'''

import math

hipotenusaMath = math.hypot(catetoAdjacente, catetoOposto)
print('O valor da hipotenusa, utilizando o método Math é: {:.2f}'.format(hipotenusaMath))
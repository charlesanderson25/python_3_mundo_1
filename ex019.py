#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

angulo = float(input('Informe o valor do ângulo em graus: '))

radianos = math.radians(angulo)
print(radianos)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print('O valor do Seno é: {:.2f} \n o valor do Cosseno é: {:.2f} \n O valor da Tangente é {:.2f}'.format(seno, cosseno, tangente))


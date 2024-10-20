# Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros

n = int(input('Informe um valor numérico em metros'))

centimetros = n * 100
milimetros = n * 1000

print('A metragem informada em centímetros é {} \n A metragem informada em milímetros é {}'.format(centimetros, milimetros))
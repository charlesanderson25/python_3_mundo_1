#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celcius = int(input('Informe a temperatura atual em graus Celcius:'))

fahrenheit = int(celcius * (9/5) + 32)

print('A temperatura informada em Celcius é exatamente {}'.format(fahrenheit),'°F')
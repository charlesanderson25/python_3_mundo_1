#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kmPercorrido = float(input('Informe q quantidade de quilômetros percorridos:'))
diasAlugado = int(input('Informe a quantidade de dias de aluguel:'))

precoKm = kmPercorrido * 0.15
precoDias = diasAlugado * 60

precoTotal = precoKm + precoDias

print('O valor total do aluguel a pagar é de R$ {:.2f}'.format(precoTotal))
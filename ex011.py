# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
# Considere: 
# U$ 1,00 = 3,27

d = float(input('Informe o valor atual em reais contido na sua carteira: R$'))

dolar = float(d / 3.27)

print('Com esse valor você consegue comprar: {:.2f} dólares'.format(dolar))
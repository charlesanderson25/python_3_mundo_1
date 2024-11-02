#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

velocidadeCarro = int(input('Informe a velocidade atual do carro:'))

limiteVelocidade = 80

if velocidadeCarro > limiteVelocidade:
    km_acima = velocidadeCarro - limiteVelocidade
    multa = float(km_acima * 7)
    print('Você ultrapassou a velocidade permitida para a via.')
    print('A multa será de R$ {:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade da via. Dirija com segurança!')

#-----------------------------------------------------------------------------

velocidadeCar = int(input('Informe a velocidade atual do seu carro:'))

if velocidadeCar > 80:
    multa = float(velocidadeCar - 80) * 7
    print('Você ultrapassou o limite de velocidade da via! Será Multado!')
    print('O valor da multa é de R$ {:.2f}'.format(multa))
else:
    print('Você está dentro da velocidade da via, dirija com segurança!')

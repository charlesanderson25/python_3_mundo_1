#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

distancia = int(input('Informe a distância de sua viagem em km:'))

viagemCurta = 200
precoViagemCurta = distancia * 0.50
precoViagemLonga = distancia * 0.45

if distancia <= viagemCurta:
    print('O preço de sua viagem foi de R$ {:.2f}'.format(precoViagemCurta))
else:
    print('O preço de sua viagem foi de R$ {:.2f}'.format(precoViagemLonga))



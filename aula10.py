#Estruturas Condicionais

tempo = int(input('Informe quantos anos tem seu carro:'))

if tempo > 10:
    print('Seu carro está velho')
else:
    print('Seu carro é novo')
print('--FIM--')

########################################################

computador = int(input('Informe quantos anos tem o seu computador:'))

print('Computador Novo' if computador < 3 else 'Computador Velho')
print('--FIM--')

########################################################

nome = str(input('Informe seu primeiro nome:'))

if nome == 'Charles':
    print('Que nome bonito! Parabéns')
else:
    print('Seu nome é tão normal!')
print('Tenha um ótimo dia! ')

##########################################################

n1 = float(input('Informe a primeira nota'))
n2 = float(input('Informe a segunda nota'))

media = (n1 + n2) / 2

print('Sua média foi de: {}'.format(media))

if media >= 7.5:
    print('Parabéns, você foi aprovado!')
else:
    print('Você foi reprovado!')
print('Ótimo dia!')
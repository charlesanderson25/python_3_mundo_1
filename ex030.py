#Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random

nrUsuario = int(input('Informe um número inteiro entre 0 e 5:'))

numeroPC = random.randint(1, 5)

print('O número sorteado foi: {}'.format(numeroPC))

if nrUsuario == numeroPC:
    print('Parabéns! Você acertou o número sorteado.')
else:
    print('Você errou o número sorteado, tente outra vez. :(')
print('--FIM do Joguinho--')
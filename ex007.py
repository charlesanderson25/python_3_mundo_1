# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada

n = int(input('Informe um valor numérico:'))

dobro = n * 2
triplo = n * 3
raizQuadrada = n ** (1/2)

print('O dobro do número informado é {} \n o triplo do número informado é {} \n a raiz quadrada do número informado é: {:.3f}'. format(dobro, triplo, raizQuadrada))
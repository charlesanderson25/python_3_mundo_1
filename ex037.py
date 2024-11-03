#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

a = float(input('Informe o tamanho da primeira reta:'))
b = float(input('Informe o tamanho da segunda reta:'))
c = float(input('Informe o tamanho da terceira reta:'))

if a + b > c and a + c > b and b + c > a:
    print('Todas condições atendidas, essas retas podem formar um triângulo!')
else:
    print('\033[31mUma ou mais condições não foram atendidas, essas retas não podem formar um triângulo!')

# Cor vermelha no texto: \033[31m


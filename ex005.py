multiplicacao = 25*3
print(multiplicacao)

raizQuadrada = 81**(1/2)
print(raizQuadrada)

raizCubica = 27**(1/3)
print(raizCubica)

print('oi'*5)

##################################################

n1= int(input('Informe um valor numérico:'))
n2= int(input('Informe outro valor numérico:'))

s = n1 + n2
sub = n1 - n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
rs = n1 % n2
ex = n1 ** n2

print('O resultado da soma é {} e da subtração é {}'.format(s, sub))
print('O resultado da multiplicação é {}, da divisão é {}, divisão inteira: {} e resto da divisão: {} \n O resultado da divisão com três casas decimais é: {:.3f}'.format(m, d, di, rs, d))
print('O resultado da exponenciação é: {}'.format(ex))
print('O resultado da divisão com três casas decimais é: {:.3f}'.format(d))

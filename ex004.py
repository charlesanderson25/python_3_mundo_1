dado = input('Digite qualquer valor')

tipo = type(dado)

print('O tipo primitivo desse valor é: {}'.format(tipo))

resultado = (dado.isspace())
resultado1 = (dado.isnumeric())
resultado2 = (dado.isalpha())
resultado3 = (dado.isalnum())
resultado4 = (dado.isupper())
resultado5 = (dado.islower())
resultado6 = (dado.istitle())

print('Só tem espaços? {}'.format(resultado))
print('É um número? {}'.format(resultado1))
print('É alfabético? {}'.format(resultado2))
print('É alfanumérico? {}'.format(resultado3))
print('Está em maiúsculas? {}'.format(resultado4))
print('Está em minúsculas? {}'.format(resultado5))
print('Está capitalizada? {}'.format(resultado6))

# print('Os resultados são: {}, {}, {}, {}, {}, {}, {}'.format(resultado, resultado1, resultado2, resultado3, resultado4, resultado5, resultado6))
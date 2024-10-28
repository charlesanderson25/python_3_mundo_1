#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nomeCompleto = str(input('Informe seu nome completo:')).strip()

primeiroNome = nomeCompleto.split()[0]
ultimoNome = nomeCompleto.split()[-1]

print('O primeiro nome é: {}'.format(primeiroNome))
print('O último nome é: {}'.format(ultimoNome))
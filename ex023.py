# Crie um programa que leia o nome completo de uma pessoa e mostre:

# – O nome com todas as letras maiúsculas e minúsculas.

# – Quantas letras ao todo (sem considerar espaços).

# – Quantas letras tem o primeiro nome.

nome = str(input('Informe seu nome completo:'))

maiusculas = nome.upper()
minusculas = nome.lower()

print('O seu nome com todas as letras maiúsculas é:',maiusculas)
print('O seu nome com todas as letras minúsculas é',minusculas)

print(len(nome))

juntarNome = '-'.join(nome)

print(juntarNome)

print('Seu nome tem:',len(juntarNome),'letras')

dividir = nome.split()

print(dividir)

letrasPrimeiroNome = len(dividir[0])

print('Seu primeiro nome tem:',letrasPrimeiroNome,'letras.')
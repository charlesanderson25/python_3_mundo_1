#Manipulando strings

frase = 'Curso em Video Python'

print(frase[9])

print(frase[9:13])

print(frase[9:21])

print(frase[9:21:2]) # salta de 2 em 2 posições 

print(frase[:5])

print(frase[15:])

print(frase[9::3]) # salta de 3 em 3 posições

print(len(frase)) # comprimento 

print(frase.count('o')) # contagem do caracter informado

print(frase.count('o', 0, 13)) # contagem caracter informando entre as posições informadas

print(frase.find('deo')) # qual posição começa a string informada

print(frase.find('Android')) # valor -1 no python é o retorno para NULL - não encontrada

print('Curso' in frase) # retorna boolean 

print(frase.replace('Python', 'Android'))

print(frase.upper())

print(frase.lower())

print(frase.capitalize()) # transforma tudo em minúsculas e transforma a primeira palavra com a primeira letra em maiúscula

print(frase.title()) # transforma a primeira letra de cada palavra em maiúsculo 

print(frase.strip()) # remove os espaços inúteis ante e após a string

print(frase.rstrip()) # remove os espaços inúteis à direita

print(frase.lstrip()) # remove os espaços inúteis à esquerda

print(frase.split()) # divide a string

print('-'.join(frase)) #juntar as strings com traço
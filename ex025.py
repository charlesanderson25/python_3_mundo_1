#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

nomeCidade = str(input('Informe o nome da sua cidade:'))

removeEspacosDireita = nomeCidade.rstrip()

removeEspacosEsquerda = removeEspacosDireita.lstrip()

maiuscula = removeEspacosEsquerda.upper()

verificaCondicao = 'SANTO' in maiuscula

print(verificaCondicao)


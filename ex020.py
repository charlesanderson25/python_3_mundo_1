# Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.

import random

aluno1 = input('Informe o nome do primeiro aluno: ')
aluno2 = input('Informe o nome do segundo aluno: ')
aluno3 = input('Informe o nome do terceeiro aluno: ')
aluno4 = input('Informe o nome do quarto aluno: ')

alunos = [aluno1, aluno2, aluno3, aluno4]

sorteio = random.choice(alunos)

print('O nome escolhido é: {}'.format(sorteio))

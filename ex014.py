# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento

salario = float(input('Informe o valor do seu salário: '))

aumento = salario * 0.15

novoSalario = salario + aumento

print('O valor do seu nono salário com aumento de 15% é: R$ {:.2f}'.format(novoSalario))
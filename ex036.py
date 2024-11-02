#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input('Informe o valor do seu salário R$:'))

aumento10 = salario * 0.10
aumento15= salario * 0.15

novoSalario10 = salario + aumento10
novoSalario15 = salario + aumento15

if salario <= 1250:
    print('O seu novo salário após aumento é de R$ {}'.format(novoSalario15))

if salario > 1250:
    print('O seu novo salário após o aumento é de R$ {}'.format(novoSalario10))

# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

preco = float(input('Informe o preço do produto: '))

desconto = preco * 0.05

valorProduto = preco - desconto

print('O valor do produto com 5% de desconto é: R$ {:.2f}'.format(valorProduto))


# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinra necessária para pintá-lo, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))

area = largura * altura

qtdTinta = 1 * (area / 2)

print('A área para pintura é de: {} '.format(area), 'metros')
print('A quantidade de tinta necessária é de {:.2} '.format(qtdTinta), 'litros')



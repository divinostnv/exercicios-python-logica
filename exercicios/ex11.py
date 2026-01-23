#faça um programa que leia a largura e a altura de um parede em metros, e calcule a quantidade de tinta necesaria para -
#pintala, sabendo quer cada litro de tinta pinta uma area de 2m²
largura= float(input('Digite a largura em metros: '))
altura= float(input('Digite a altura em metros: '))
tinta= (largura*altura)/2
print(f'O tamanho da sua parede é {largura*altura:.3f}m²\n'
      f'e para pintar será necessario L{tinta:.3f} de tinta')
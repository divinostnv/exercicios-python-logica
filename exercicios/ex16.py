#Crie um programa que leia um numero real qualquer pelo teclado e mostre na tela sua porção inteira
from math import trunc
numero= float(input('Digite um numero qualquer: '))
print(f'Seu numero é {numero} e a sua porção inteira é {trunc(numero)}')
"""print(f'Seu numero é {numero} e a sua porção inteira é {int(numero)}')"""
#faça um programa que leia o comprimento de um cateto oposto e do cateto adjacente de um triangulo retangulo , calcule -
# e mostre o comprimento da hipotenusa.
"""import math
co= float(input("digite o cateto oposto:"))
ca= float(input("digie o cateto adijacente:"))
hipo=math.hypot(ca,co)
print(f'a hipotenusa é igual {hipo:.2f}')"""
#ou
co= float(input('Digite o cateto oposto: '))
ca= float(input('Digite o cateto adjacente: '))
hipo= (co**2 + ca**2)**(1/2)
print(f'A hipotenusa é igual {hipo:.2f}')
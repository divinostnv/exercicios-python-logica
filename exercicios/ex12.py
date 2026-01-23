#faça um algoritimo que leiao preço de um produto e mostre o novo preço com 5% de desconto.
valor = float(input("valor que vc quer conseguir o desconto:"))
desconto= valor-((valor/100)*5)
print(f'com 5% de desconto o seu valor ficará {desconto}')
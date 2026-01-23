#faça um algoritimo que leia um salario e mostre com 15% de aumento.
salario= float(input('Digite seu salario para dar 15% de aumento: '))
aumento= ((salario/100)*15)+salario
print(f'O salario com 15% de aumento ficará {aumento}')
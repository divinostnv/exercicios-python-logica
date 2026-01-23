#Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários
# superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
salario=float(input('Digite o seu salario: '))
if salario<1250:
    aumento='15%'
    valor= ((salario/100)*15)+salario
else:
    aumento='10%'
    valor= ((salario/100)*10)+salario
print(f'Seu salário de \033[31m{salario}\033[m terá um aumento de {aumento} e ficará no valor de \033[32m{valor}')
#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. Pergunte o valor da casa, o salário -
#do comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 30% do salário ou então o empréstimo -
#será negado.
casa= float(input('Digite o valor da casa: '))
salario= float(input('Digite o valor do salário: '))
anos= int(input('Em quantos anos deseja pagar a casa?'))
calculo= (salario/100)*30
anos1= casa/(anos*12)
print(f'O valor da casa é {casa} e para ser paga em {anos} anos')
print(f'A prestação ficara {anos1}')
if calculo>anos1:
    print('\033[32mSua compra foi aprovada!')
else:
    print('\033[31mSua compra foi negada!')
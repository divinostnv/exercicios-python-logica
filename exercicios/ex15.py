#Escreva um programa que pergunte a quantidade de Km pecorridos por um carro alugado e a quantidade de dias pelos quais-
# ele foi alugado. Calcule o preço a pagar sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
dias= int(input("quantidade de dias com o carro alugado:"))
km= float(input("quantidade de km's pecorridos:"))
n1= dias*60
n2= km*0.15
n3= n2+n1
print(f" com {dias} dias pecorridos vc terar um gasto de {n1} reais\n com {km} km's rodados terar um gasto de {n2} reais"
      f"com gasolina\n somando {n3} reais gastos")
# Exercício Python 067: Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido 
# quando o número solicitado for negativo.
valor=0
cont=0
valor=int(input("Deseja ver a tabuada de qual valor: "))
while True:
    cont=0
    if valor>=0:
        while cont<11:
            print(f'{valor} X {cont} = {valor*cont}')
            cont+=1
    if valor>=0:
        valor= int(input("Qual outro valor deseja ver a tabuada: "))
    else:
        print("finalizado...")
        break
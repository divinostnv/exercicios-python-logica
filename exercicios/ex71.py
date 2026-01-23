dinheiro=int(input("Quantos dinheiros você quer sacar? "))
nota50=0
nota20=0
nota10=0
nota1=0

while True:
    while dinheiro >= 50:
        nota50+=1
        dinheiro-=50
    if nota50>=1:
        print(f"Você receberá {nota50} notas de 50R$ ")
    while dinheiro>=20:
        nota20+=1
        dinheiro-=20
    if nota20 >=1:
        print(f"Você receberá {nota20} notas de 20R$ ")
    while dinheiro>=10:
        nota10+=1
        dinheiro-=10
    if nota10 >=1:
        print(f"Você receberá {nota10} notas de 10")
    while dinheiro>=1:
        nota1+=1
        dinheiro-=1
    if nota1>=1:
        print(f"Você receberá {nota1} moedas de real 1")
    break
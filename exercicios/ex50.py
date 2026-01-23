#Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor -
# digitado for ímpar, desconsidere-o.
print('Digite seis numeros inteiros para ser mostrado a soma ente os pares')
soma=0
cont=0
for n in range(0,6):
    numeros= int(input("digite um numero: "))
    if numeros%2==0:
        soma+=numeros
        cont+=1
print(f'a soma entre os {cont} numeros pares é {soma}')

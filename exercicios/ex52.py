# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.
numero=int(input('Digite um numero: '))
cont=0
for n in range(1,numero+1):

    if numero%n==0:
        cont+=1
        print(f'\033[34m{n}', end=' ')
    elif n%numero!=0:
        print(f'\033[31m{n}', end=' ')
if cont<=2:
    primo=f'O numero é primo foi dividido {cont} vezes'
else:
    primo=f'O numero não é primo, foi dividido {cont} vezes'
print(f'\n\033[m{primo}')
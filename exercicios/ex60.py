#Faça um programa que leia um número qualquer e mostre o seu fatorial.
numero=int(input('Digite o numero que deseja saber o fatorial: '))
n= numero
fatorial=1
while n>0:
    print(f'{n}', end='')
    print(' x ' if n>1 else ' = ', end='')
    n-=1
    fatorial*=numero
print(fatorial)
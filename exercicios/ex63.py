#Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
"""Nanterior=0
Nsucessor=1
cont=0
soma=1
while cont<10:
    print(f"{Nanterior}", end=', ')
    soma=Nanterior+Nsucessor
    Nanterior=Nsucessor
    Nsucessor=soma
    cont+=1
    if cont>10:
        while mais!=0:
            mais=int(input('Deseja mostrar mais quantos numeros: '))
            cont=1
            while cont<=mais:
                print(f"{Nanterior}", end=', ')
                soma=Nanterior+Nsucessor
                Nanterior=Nsucessor
                Nsucessor=soma
                cont+=1"""
Nanterior = 0
Nsucessor = 1
cont = 0
soma = 1

while cont < 10:
    print(f"{Nanterior}", end=', ')
    soma = Nanterior + Nsucessor
    Nanterior = Nsucessor
    Nsucessor = soma
    cont += 1

mais = int(input('Deseja mostrar mais quantos números? (0 para sair): '))

while mais != 0:
    for _ in range(mais):
        print(f"{Nanterior}", end=', ')
        soma = Nanterior + Nsucessor
        Nanterior = Nsucessor
        Nsucessor = soma
    mais = int(input('Deseja mostrar mais quantos números? (0 para sair): '))
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada
import random
n1= str(input("digite o primeiro nome: "))
n2= str(input("digite o segundo nome: "))
n3= str(input("digite o terceiro nome: "))
n4= str(input("digite o quarto nome: "))
lista= [n1, n2, n3, n4]
posição= random.sample(lista, k=4)
print(f'a ordem da a sua lista ta será \n{posição}')
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
n1= str(input("digite o primeiro nome"))
n2= str(input("digite o segundo nome"))
n3= str(input("digite o terceiro nome"))
n4= str(input("digite o quarto nome"))
L= [n1,n2,n3,n4]
random= random.choice(L)
print(f'o aluno escolhido é {random}')
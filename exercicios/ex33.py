#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1= int(input('Digite o primeiro valor: '))
n2= int(input('Digite o segundo valor: '))
n3= int(input('Digite o terceiro valor: '))
if n2>n1<n3:
    menor= n1
if n1>n2<n3:
    menor= n2
if n1>n3<n2:
    menor=n3
if n2<n1>n3:
    maior= n1
if n1<n2>n3:
    maior=n3
if n1<n3>n2:
    maior=n3
print(f'O maior numero digitado foi {maior}')
print(f'O menor numero digitado foi {menor}')
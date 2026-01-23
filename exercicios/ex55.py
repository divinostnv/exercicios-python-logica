# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.
n=''
maior=0
menor=0
for n in range(1,6):
    peso= float(input(f'Digite o peso da {n}º pessoa: '))
    if peso>maior:
        maior=peso
    if menor==0 or peso<menor:
        menor=peso
print(f'O maior peso digitado foi {maior}')
print(f'O menor peso digitado foi {menor}')
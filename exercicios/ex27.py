#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
nome= str(input('Digite seu nome: ')).title().strip()
n= nome.split()
print(f'O primeiro nome é {n[0]}')
print(f'O ultimo nome é {n[-1]}')
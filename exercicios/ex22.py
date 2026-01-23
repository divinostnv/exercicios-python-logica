#Crie um programa que leia o nome completo de uma pessoa e mostre:
# O nome com todas as letras maiúsculas e minúsculas.
# Quantas letras ao todo (sem considerar espaços).
# Quantas letras tem o primeiro nome.
nome= str(input('Digite seu nome completo: '))
n= nome.split()
n1= ''.join(nome)
print(f'Todo em maiusculo, {nome.upper()}')
print(f'Todo em minusculo {nome.lower()}')
print(f'Quantas letras? {(len(n1))}')
print(f'Quantas letras tem o primeiro nome? {len(n[0])}')
print(f'O ultimo nome é? {n[len(n)-1]}')
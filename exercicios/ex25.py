#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome=str(input('Digite o seu nome: ')).title().strip()
n= 'Silva' in nome
if n== True:
    print(f'o nome {nome}, tem Silva')
else:
    print(f'O nome {nome}, não tem Silva')
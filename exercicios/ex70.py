#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.
cont=0
valorTotal=0
maior1000=0
maisBarato=''
valorBarato=0
while True:
    cont+=1
    nomeProd=str(input(f'Qual o nome do {cont}º produto: ')).title().strip()
    valorProd=float(input(f'Qual o valor do {cont}º produto: '))
    continuar=str(input(f'Deseja continuar e adicionar mais produtos? [S/N] ')).upper().strip()
    valorTotal+=valorProd
    if valorProd> 1000:
        maior1000+=1
    elif cont==1:
        maisBarato=nomeProd
        valorBarato=valorProd
    elif valorProd<valorBarato:
        maisBarato=nomeProd
    if continuar in 'Ss':
        print(f"-_"*30)
    elif continuar in "Nn":
        print(f"-_"*30)
        if cont==1:
            print('Erro foi informado apenas um produto')
        else:
            print(f'O valor total da compra é de {valorTotal}')
            print(f'{maior1000} produtos custão mais de 1000R$')
            print(f'O nome do produto mais barato é {maisBarato}')
        break
    else:
        print('Caractere invalido para validação da continuidade do programa, comece novamente, por favor!!')
        break


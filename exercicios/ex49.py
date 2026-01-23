#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
n=int(input('Digite o numero que deseja saber a tabuada: '))
for c in range(0,11):
    print(f'{n} * {c} = {n*c}')
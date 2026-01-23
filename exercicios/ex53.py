#Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
palavra=str(input('Digite uma frase: ')).strip().lower()
espaço= palavra.replace(' ', '')
coisa=''
for n in range(len(espaço)-1,-1,-1):
    coisa+= espaço[n]
if coisa== palavra:
    print(f'A palavra {espaço} é um palindromo, seu inverso é {coisa} ')
else:
    print(f'A palavra {espaço} não é um palindromo, seu inverso é {coisa}')
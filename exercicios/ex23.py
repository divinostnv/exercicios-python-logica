#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.
espaço= '0000'
numero= str(input('Digite um numero de 0 a 9999: '))
soma= espaço+numero
print(f'Sua unidade de milhar é {soma[-4]}')
print(f'Sua centena é {soma[-3]}')
print(f'Sua dezena é {soma[-2]}')
print(f'Sua unidade é {soma[-1]}')
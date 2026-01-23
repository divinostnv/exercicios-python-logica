#Escreva um programa que leia dois números inteiros e compare-os. mostrando na tela uma mensagem:
#O primeiro valor é maior
#O segundo valor é maior
#Não existe valor maior, os dois são iguais
numero1= int(input('Digite o primeiro numero: '))
numero2= int(input(('Digite o segundo numero: ')))
if numero1== numero2:
    maior= 'Os numero são iguais, não existe valor maior'

elif numero1> numero2:
    maior='O primeiro numero é maior que o segundo'

elif numero2>numero1:
    maior= 'O segundo numero é maior que o primeiro'

print(maior)
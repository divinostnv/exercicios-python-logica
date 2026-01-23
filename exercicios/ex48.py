#Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo -
# de 1 até 500.
soma=0
cont=0
for n in range(0,501):
    if n % 2 !=0:
        if n % 3==0:
            cont+=1
            soma+=n

print(f'foram solicitados {cont} valores, e a soma entre eles é {soma}')
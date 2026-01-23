#Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
import time

n=''
for n in range(0,51):
    if n%2==0:
        print(n, end='  ')
        time.sleep(0.5)
print('Acabou')
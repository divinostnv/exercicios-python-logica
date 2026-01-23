#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
#descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random
import time

print('Que tal tentar adivinhar o numero que o computador pensou?')
time.sleep(1.5)
numero= int(input('Digite um numero de 0 a 5: '))
print('\033[34mprocessando...\033[m')
time.sleep(1)
computador=random.randint(0,5)
if numero==computador:
    print(f'\033[33mVocê acertou, computador jogou {computador}')
else:
    print(f'\033[31mEu pensei no numero {computador} não no numero {numero}')
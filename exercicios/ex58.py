#Melhore o jogo do DESAFIO 028 onde o computador vai "pensar" em um número entre 0 e 10. Só que agora o -
#  jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import time
import random
computador= random.randint(0,10)
tentativas=0
print('O computador pensou em um numero, que tal tentar acertar? ')
time.sleep(1)
palpites=''
while palpites!= computador:
    palpites=int(input('Digite um numero: '))
    tentativas+=1
    if palpites < computador:
        print('o numero pensado pelo computador é \033[31mmaior\033[m')
    elif palpites> computador:
        print('O numero pensado pelo computadro é \033[34mmenor\033[m')
print(f'Você venceu, em {tentativas} tentativas')
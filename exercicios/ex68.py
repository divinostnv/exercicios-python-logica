# Exercício Python 068: Faça um programa que jogue par ou ímpar com o computador.
# O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias
# consecutivas que ele conquistou no final do jogo.
import random
numero=int(input("digite um numero: "))
escolha= str(input('Par ou impar[P/I]: ')).upper().strip()
computador= random.randint(0,11)
cont=0
while True:
    if (numero+computador)%2==0:
        parouimpar='par'
    else:
        parouimpar='impar'
    if escolha[0] == 'P':
        escolha='par'
    elif escolha[0] == 'I':
        escolha='impar'
    else:
        print("Caractere invalido")
        print("-_"*30)
        break
    if escolha== parouimpar:
        print(f'\033[32mVocê ganhou! você jogou {numero} e o computador jogou {computador} e deu {parouimpar}\033[m')
        cont+=1
        print("-_"*30)
    if escolha== parouimpar:
        numero=int(input("\033[mdigite um numero: "))
        escolha= str(input('Par ou impar[P/I]:')).upper().strip()
    else:
        print(f'\033[31mVocê perdeu! computador jogou {computador} e você {numero} e deu {parouimpar}\033[m')
        if cont>1:
            print(f'\033[32mVocê ganhou {cont} vezes. Parabéns!\033[m')
        elif cont==1:
            print('\033[33mvocê ganhou só 1 vez\033[m')
        else:
            print('\033[31mVocê não ganhou nenhuma vez, mais sorte da proxima vez!\033[m')
        print("-_"*30)
        break
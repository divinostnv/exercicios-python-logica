import random
import time

escolha=int(input('[ 0 ] pedra\n'
                  '[ 1 ] papel\n'
                  '[ 2 ] tesoura\n'
                  'Digite sua escolha: '))
print('\033[1;31mJO')
time.sleep(1.0)
print('\033[1;32mKEN')
time.sleep(1.0)
print('\033[1;34mPOO!!!\033[m')
time.sleep(1.0)
computador= random.randint(0,2)
if computador==0:
    escolhapc= 'Pedra'
elif computador==1:
    escolhapc= 'Papel'
elif computador==2:
    escolhapc= 'Tesoura'
if escolha==0:
    escolha1= 'Pedra'
elif escolha==1:
    escolha1= 'Papel'
elif escolha==2:
    escolha1= 'Tesoura'
if computador==escolha:
    print(f'\033[1;33mEmpatou o computador também escolheu {escolhapc}\033[m')
elif escolha==0 and computador==2 or escolha==1 and computador==0 or escolha==2 and computador==1:
    print(f'\033[1;32mVocê ganhou! você escolheu {escolha1} e o computador {escolhapc}\033[m')
elif computador==0 and escolha==2 or computador==1 and escolha==0 or computador==2 and escolha==1:
    print(f'\033[1;31mVocê perdeu! computador escolheu {escolhapc} e você {escolha1}\033[m')
else:
    print('opção invalida, tente novamente')
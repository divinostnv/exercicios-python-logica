import time
n1= int(input('Digite o primeiro valor: '))
n2= int( input('Digite o segundo valor: '))
time.sleep(0.5)
n=''
sair= 5
while n != sair:
    print(f'O que deseja fazer com {n1} e {n2}: ')
    n= int( input('[1] somar\n'
                  '[2] multiplicar\n'
                  '[3] maior valor\n'
                  '[4] novos numeros\n'
                  '[5] sair\n'
                  'Escolha uma opção: '))
    print('-_-' * 15)
    if n==1:
        print(f'{n1}+{n2}= {n1+n2}')
        print('-_-' * 15)
        time.sleep(2)
    elif n==2:
        print(f'{n1}x{n2}={n1*n2}')
        print('-_-' * 15)
        time.sleep(2)
    elif n==3:
        if n1>n2:
            print(f'O maior é {n1}')
            print('-_-' * 15)
            time.sleep(2)
        elif n1<n2:
            print(f'o maior é {n2} ')
            print('-_-' * 15)
            time.sleep(2)
        elif n1==n2:
            print('Os numeros são iguais, não possui maior')
            print('-_-' * 15)
            time.sleep(2)
    elif n==4:
        n1 = int(input('Digite o primeiro valor: '))
        n2 = int(input('Digite o segundo valor: '))
        print('-_-' * 15)
        time.sleep(2)
    elif n!=sair:
        print('Opção invalida. tente novamente')
        print('-_-' * 15)
print('Finalizando...')
time.sleep(1)
print('Volte sempre que precisar!')
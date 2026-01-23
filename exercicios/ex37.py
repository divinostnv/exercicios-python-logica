#Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de -
# conversão: 1 para binário, 2 para octal e 3 para hexadecimal.
numero= int(input('Digite um numero inteiro qualquer:'))
escolha= int(input('escolha uma opção\n'
                   '[ 1 ] Binário\n'
                   '[ 2 ] Octal\n'
                   '[ 3 ] hexadecimal\n'
                   'Digite o numero da sua escolha: '))
if escolha ==1:
    binario= bin(numero)
    print(f'Sua conversão para binario é {binario.replace('0b', '')}')
elif escolha==2:
    octal= oct(numero)
    print(f'Sua coversão para octal é {octal.replace('0o','')}')
elif escolha==3:
    hexadecimal= hex(numero)
    print(f'Sua conversão para hexadecimal é {hexadecimal.replace('0x','')}')
else:
    print('Algo deu errado, tente novamente')
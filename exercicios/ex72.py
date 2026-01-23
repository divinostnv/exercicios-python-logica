Numeros=('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
escolha=0
while True:
    escolha=int(input("digite um numero entre 0 e 20: "))
    if 20>escolha>0 :
        cont=Numeros[escolha]
        print(f'Você escolheu o numero \033[33m{cont}')
        break
    else:
        print('\033[31mErro, numero inválido, tente novamente\033[m')
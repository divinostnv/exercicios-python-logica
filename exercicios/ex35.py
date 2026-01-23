#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
primeiro= float(input('Digite o primeiro seguimento: '))
segundo= float(input('Digite o segundo seguimento: '))
terceiro= float(input('Digite o terceiro seguimento: '))
if primeiro+segundo>terceiro or segundo+terceiro> primeiro or terceiro+primeiro> segundo:
    print('Pode se formar um triangulo')
else:
    print('Não pode se formar um triangulo')
# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o botando cor no input se ele for par e uma cor diferente se for impar.

print('Digite seis números inteiros para ser mostrado a soma entre os pares')

soma = 0
cont = 0

for n in range(0, 6):
    while True:
        try:
            numero = int(input('Digite um número: '))
            break
        except ValueError:
            print('Valor inválido. Por favor, digite um número inteiro.')

    if numero % 2 == 0:
        print(f'\033[34mNúmero par: {numero}\033[0m')
        soma += numero
        cont += 1
    else:
        print(f'\033[31mNúmero ímpar: {numero}\033[0m')

print(f'A soma entre os {cont} números pares é {soma}')
# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, mostre os 10 primeiros termos dessa -
# progressão.
primeiro= int(input('Primeiro termo: '))
razao=int(input('Qual a razão: '))
ultimo= (primeiro+razao)*10
for n in range(primeiro,ultimo,razao):
    print(n, end=' → ')
print('acabou')
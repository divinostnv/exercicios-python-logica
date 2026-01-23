#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cidade=str(input('Digite o nome da cidade em que você nasceu: ')).title().strip()
espaço= cidade.split()
santo= 'Santo' in espaço[0]
if santo== True:
    print(f'A cidade {cidade} começa com santo')
else:
    print(f'A cidade {cidade} não começa com santo')
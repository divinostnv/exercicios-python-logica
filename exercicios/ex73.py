brasileirão= ('Palmeiras', 'Flamengo', 'Bragantino', 'Cruzeiro', 'Fluminsense', 'Atlético Mineiro', 'Bahia', 'Botafogo', 'Ceará SC', 'Corinthians', 'Fortaleza', 'Mirassol', 'Internacional', 'EC Vitoria', 'Grêmio', 'São Paulo', 'Vasco da Gama', 'Juventude', 'Santos', 'Sport Recife')
print('\033[31mOs 5 primeiros classificados são:\033[m ')
for c in range(0,5):
    print(brasileirão[c])
print('\033[31mOs quatro ultimos são:\033[m ')
for c in range(-4,0,1):
    print(brasileirão[c])
print(sorted(brasileirão))
print(f'\033[31mO vasco está na posição {brasileirão.index('Vasco da Gama')+1}\033[m')
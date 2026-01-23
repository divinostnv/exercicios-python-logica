import random
maior=0
menor=0
numeros= (1,2,3,4,5,6,7,8,9,10)
sorteio1= random.choice(numeros)
sorteio2= random.choice(numeros)
sorteio3= random.choice(numeros)
sorteio4= random.choice(numeros)
sorteio5= random.choice(numeros)
sorteados= (sorteio1, sorteio2, sorteio3, sorteio4, sorteio5)
ordem=sorted(sorteados)
print(f'Os cinco numeros sorteados foi {ordem}')
print(f'E o menor numero do sorteio foi {ordem[0]}')
print(f'E o maior numero do sorteio foi {ordem[4]}')
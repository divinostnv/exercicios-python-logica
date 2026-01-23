P= int(input('Qual o primeiro termo? '))
R= int(input('Qual a razão? '))
termo=P
cont=1
while cont<=10:
    print(f"{termo}", end=' ')
    termo += R
    cont+=1
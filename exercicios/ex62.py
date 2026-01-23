#Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerrará quando -
# ele disser que quer mostrar 0 termos.
P= int(input('Qual o primeiro termo? '))
R= int(input('Qual a razão? '))
termo=P
cont=1
mais=''
while cont<=10 and mais!=0:
    print(f"{termo}", end=' ')
    termo += R
    cont+=1
    if cont>10:
        while mais!=0:
            mais = int(input('\nVocê quer mostrar mais termos?' ))
            cont=1
            while cont<=mais:
                print(f"{termo}", end=' ')
                termo+=R
                cont+=1
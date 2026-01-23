#Crie um programa que leia vários números inteiros pelo teclado. No final da
# execução, mostre a média entre todos os valores e qual foi o maior e o 
# menor valores lidos. O programa deve perguntar ao usuário se ele quer ou
#  não continuar a digitar valores.
continuar=''
cont=0
soma=0
maior=0
menor=0
while 'NÃO' !=continuar!='N':
    numero= str(float( input('Digite um numero: ')))
    cont+=1
    soma+=numero
    media=soma/cont
    if cont==1:
        maior=numero
        menor=numero
    else:
        if numero>maior:
            maior=numero
        elif numero<menor:
            menor=numero
    if numero>-100000:
        continuar=str(input('Deseja continuar[S/N]?')).upper()
        while continuar not in 'SN':
            continuar=str(input('Tente novamente, deseja continuar [S/N]?')).upper()
print(f'A soma dos numeros é {soma:.0f} e a media é {media}')
print(f'O maior valor foi {maior}')
print(f'O menor valor foi {menor}')
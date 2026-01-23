#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não -
#  atingiram a maioridade e quantas já são maiores.
import datetime

anoatual = datetime.date.today().year
contvelho=0
contnovo=0
contnnascidos=0
for n in range (1,8):
    ano =int(input(f'Digite o ano que a {n}º pessoa nasceu: '))
    if anoatual-ano<18:
        contvelho+=1
    else:
        contnovo+=1
if contvelho>=0:
    print(f'temos {contvelho} pessoas menore de idade')
if contnovo>=0:
    print(f'temos {contnovo} pessoas maiores de idade')
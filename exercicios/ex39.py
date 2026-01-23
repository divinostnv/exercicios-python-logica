#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se -
# alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa -
# também deverá mostrar o tempo que falta ou que passou do prazo.
import datetime

nascimento= int(input('Digite o ano de nascimento: '))
atual= datetime.date.today().year
idade= atual-nascimento
if idade<18:
    print(f'Calma combatente! quem nasce em {nascimento} tem {idade} anos, e terá seu alistamento daqui a {18-idade}'
          f' anos em {atual+(18-idade)}')
elif idade>18:
    print(f'Quem nasceu em {nascimento} tem {idade} anos, e tinha que ter se alistado a {idade-18} anos atrás em '
          f'{atual-(idade-18)}')
else:
    print(f'Quem nasceu em {nascimento} tem 18 anos e terá seu alistamento nesses ano de {atual}')
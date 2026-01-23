#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua
# Categoria, de acordo com a idade
import datetime
ano= int(input('Digite o ano em que você nasceu: '))
hoje= datetime.date.today().year
idade=hoje-ano
if idade<9:
    classificação= 'mirim'
elif idade< 14:
    classificação= 'Infantil'
elif 14< idade<=19:
    classifcação= 'junior'
elif 19< idade<=25:
    classificação= 'Senior'
elif idade>25:
    classificação= 'Master'
print(f'Você tem {idade}, então é {classifcação}')

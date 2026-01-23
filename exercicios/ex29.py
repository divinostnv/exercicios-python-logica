#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele
#foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade= int(input('Digite a velocidade atual do carro: '))
if velocidade>80:
    multa = (velocidade - 80) * 7
    print(f'\033[31mVocê foi multado! ultrapassou {velocidade-80} e receberá uma multa no valor de R${multa}')
else:
    print('\033[33mVocê não foi multado, parabens!')
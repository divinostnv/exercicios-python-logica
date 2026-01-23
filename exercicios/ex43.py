#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre -
# seu status, de acordo com a tabela abaixo
peso= float('Digite seu peso em KG: ')
altura= float('Digite sua altura em M')
imc= peso/(altura**2)
if imc<18.5:
    resultado= '\033[1;31mAbaixo do peso\033[m'
elif 18.5<=imc<25:
    resultado= '\033[32mno peso ideal\033[m'
elif 25<=imc<30:
    resultado= '\033[1;31msobrepeso\033[m'
elif 30<imc<40:
    resultado= '\033[31mcom obesidade, cuidado!\033[m'
else:
    resultado='\033[31mcom obesidade MORBIDA, tome bastante cuidado!\033[m'
print(f'Seu imc deu {imc:.2f}\n \033[mVocê está\033[m {resultado}')
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por
# Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
Km= float(input('Digite os Kms pecorridos na viagem: '))
if Km<=200:
    print(f'Você pagará o valor de R${Km*0.50:.2f} na passagem')
else:
    print(f'Você pagará o valor de R${Km*0.45:.2f} na passagem')
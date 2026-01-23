#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
real= float( input(' Digite quanto dinheiro você deseja converter:  R$'))
dolar= real/ 6.05
euro= real/ 6.20
libra= real/ 7.40
print(f'Com R${real:.0f}\nVocê consegue comprar:\n${dolar:.1f}\n€{euro:.1f}\n£{libra:.1f}')
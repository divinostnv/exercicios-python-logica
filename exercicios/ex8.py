#Desenvolva um programa que leia um valor em metros e converta para centimetros e milimetros
metro= float(input('Digite o valor em metros que deseja converter: '))
km = metro/1000
hm = metro/100
dam = metro/10
m = metro
dm = 10*metro
cm = 100*metro
mm = 1000*metro
print(f' seu numero = {m:.0f} \n'
      f'em Quilômetro = {km} \n'
      f'em Hectometro = {hm} \n'
      f'em Decametro = {dam} \n'
      f'em Decimetro = {dm} \n'
      f'em centimetro = {cm} \n'
      f'em milimetro = {mm}')
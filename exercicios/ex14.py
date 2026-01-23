#escreva um programa que leia a temperatura digitada em Cº e converta pra Fº.
F=float(input("graus celsius que vc deseja converter para fahrenheint? "))
C=float(input("fahrenheint que vc deseja converter para grausº celsius? "))
n1= (F*1.8)+32
n2= (C-32)/1.8
print(f'valor da conversão de graus celsiusº {n1}\n valor da conversão de fahrenheintº {n2}')
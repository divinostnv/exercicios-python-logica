#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores 'M' ou 'F'. Caso esteja errado, peça a -
# digitação novamente até ter um valor correto.
sexo=str(input('Digite seu sexo: ')).lower()
while sexo!='f' and sexo!= 'm':
    sexo= str(input('Digite seu sexo: ')).lower()
if sexo=='m':
    registro= 'Masculino'
if sexo=='f':
    registro='Feminino'
print(f'Sexo {registro} registrado com sucesso')
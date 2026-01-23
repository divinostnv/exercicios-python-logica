# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com -
# a média atingida:
#Média abaixo de 5.0: REPROVADO
#Média entre 5.0 e 6.9: RECUPERAÇÃO
#Média 7.0 ou superior: APROVADO
nota1= int(input('Digite a primeira nota: '))
nota2= int(input('Digite a segunda nota: '))
media= (nota1+nota2)/2
if media<5:
    print(f'\033[31mCom a media das notas {nota1} e {nota2} = {media}, você está reprovado!')
elif 5<media<6.9:
    print(f'\033[33mCom a media das notas {nota1} e {nota2} = {media}, você está de recuperação!')
else:
    print(f'\033[32mCom a media das notas {nota1} e {nota2} = {media}, você está aprovado!')
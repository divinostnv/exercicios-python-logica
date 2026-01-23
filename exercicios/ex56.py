#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do -
# grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
ano=0
homemv=0
idadecont=0
for n in range(1,5):
    nome=str(input(f'Digite o nome da {n}º pessoa: ')).title()
    idade=int(input(f'Digite a idade da {n}º pessoa: '))
    sexo=str(input((f'Digite o sexo da {n}º pessoa, [M/F]: '))).upper()
    print('-_'*30)
    ano+=idade
    media= ano/n
    if idade>homemv and 'M' in sexo[0]:
        homemv=idade
        velho=nome
    if 'F' in sexo[0]  and idade>=20 :
        idadecont+=1
print(f'A media das idades das {n} pessoas é {media}')
print(f'O homem mais velho é {velho} com {homemv} anos')
print(f'foi informado {idadecont} pessoas do sexo feminino com mais de 20 anos')
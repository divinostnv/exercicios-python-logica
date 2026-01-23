#Exercício Python 069: Crie um programa que leia a idade e o sexo de várias pessoas.
#  A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.
cont=0
pessoasMaior18=0
homens=0
mulheresMenos20=0
cadastro=0
sexo=''
while True:
    if sexo in 'MmFf':
        print("-_"*30)
        cont+=1
        nome=str(input(f'Digite o nome da {cont}º pessoa: '))
        idade= int(input(f'Digite a idade da {cont}º pessoa: '))
        sexo= str(input(f'Digite o sexo da {cont}º pessoa. [F/M]: ')).upper().strip()
        cadastro+=1
        continuar=str(input('Deseja contunuar? [S/N]')).upper().strip()
        if idade > 18:
            pessoasMaior18+=1
        if sexo[0] in 'M':
            homens+=1
        if sexo[0] in 'F' and idade<20:
            mulheresMenos20+=1
        if continuar== 'N':
            print("-_"*30)
            if cadastro<=0:
                print('não houve cadastro, tente novamente')
                break
            elif cadastro==1:
                print(f'foi cadastrado apenas uma pessoa')
                print(f'Sendo {pessoasMaior18} pessoas maior de 18.')
                print(f'{homens} homens')
                print(f'E {mulheresMenos20} mulheres com menos de 20 anos')
            else:
                print(f'Foram cadastradas {cadastro} pessoas')
                print(f'Sendo {pessoasMaior18} pessoas maior de 18.')
                print(f'{homens} homens')
                print(f'E {mulheresMenos20} mulheres com menos de 20 anos')
            break
    else:
        print('Erro dados invalidos, renicie o programa')
        break
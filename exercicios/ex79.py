parar=''
lista=[]
respostas = ['S','N']
while parar != 'N' :
    numero=int(input('Digite um numero para adicionar a lista: '))
    if numero not in lista:
        lista.append(numero)
    else:
        print('Numero já existente na lista. ')
    parar=str(input('deseja continuar [S/N^] ? ')).upper()
    while parar not in respostas:
        parar=str(input('deseja continuar [S/N^] ? ')).upper()
        if parar != 'S' and parar != 'N':
            print('Resposta invalida, tente novamente. ')
    lista.sort()
print(f' a sua lista é {lista}')
 parar=str(input('deseja continuar [S/N^] ? ')).upper()
    while parar not in respostas:
        parar=str(input('deseja continuar [S/N^] ? ')).upper()
        if parar != 'S' and parar != 'N':
            print('Resposta invalida, tente novamente. ')
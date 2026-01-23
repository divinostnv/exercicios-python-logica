listaProduto= ('Lápis',1.75, 'Borracha', 2, 'Caderno',15.90, 'Estojo', 25, 'Trasferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)
valor=''
print('-'*38)
print(f"{"lista de um mercado":>29}")
print('-'*38)
for n in range(0, len(listaProduto)):
    if n%2==0:
        print(f"{listaProduto[n]:.<30}", end='')
    else:
        print(f'R${listaProduto[n]:>6.2f}')
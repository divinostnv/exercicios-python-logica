nome= str(input('Digite uma palavra: ')).lower()
contv=0
contc=0
if nome in 'aeiou':
    contv+=1
else:
    contc+=1
print(f'A palavra {nome} tem {contc} consoante(s) e {contv} vogal(es).')
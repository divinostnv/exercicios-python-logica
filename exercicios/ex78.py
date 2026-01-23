lista=[]
for n in range(1,6):
    numeros=int(input(f"qual o {n}º numero? "))
    lista.append(numeros)
lista1 = lista[:]
maior=lista1.sort(reverse=True)
maior= lista1[0]
menor=lista1[4]
print(f"a sua lista é {lista}")
print(f'\no maior valor é {maior}', end=', ')
for lugar, numero in enumerate(lista):
    if maior==numero:
        print(f'no lugar {lugar+1}', end='...')
print(f'\no menor valor é {menor}', end=' ') 
for lugar, numero in enumerate(lista1):
    if menor==numero:
        print(f'no lugar {lugar+1}', end='...')
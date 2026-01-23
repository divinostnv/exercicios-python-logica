numero= (int(input(f"digite o primeiro valor: ")),
          int(input(f"digite o segundo valor: ")),
          int(input(f"digite o terceiro valor: ")),
          int(input(f"digite o ultimo valor: ")))
print(numero)
print(f'O numero 9 aparece {numero.count}')
if 3 in numero:
    print(f'O numero 3 aparece na posição {numero.index(3)+1} ')
else:
    print(f'O numero 3 não aparece na tupla')
print("Os numeros pares digitados são", end='')
for n in numero:
    if n%2==0:
        print(n, end='')

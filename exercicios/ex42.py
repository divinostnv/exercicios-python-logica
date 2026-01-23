#Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado
lado1= float(input('Digite o comprimento do primeiro lado: '))
lado2= float(input('Digite o comprimento do segundo lado: '))
lado3= float(input('Digite o comprimento do terceiro lado: '))
if lado1+lado2>lado3 and lado2+lado3>lado1 and lado3+lado1>lado2:
    if lado1== lado2 == lado3:
        triangulo= 'equilatero'
    elif lado1!=lado2!=lado3!=lado1:
        triangulo= 'isosceles'
    elif lado1!=lado2 and lado2 != lado3 and lado3 != lado1:
        triangulo= 'escaleno'
    print(f'pode se formar um triangulo {triangulo}')
else:
    print('\033[31Não se pode formar um triangulo')
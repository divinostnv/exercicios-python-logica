#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
n= float(input("digite a area do seu triangulo:"))
radians= math.radians(n)
seno= math.sin(radians)
coseno=math.cos(radians)
tangente=math.tan(radians)
print(f"seu seno é {seno:.2f}\n seu cosseno {coseno:.2f} \n sua tangente {tangente:.2f}")
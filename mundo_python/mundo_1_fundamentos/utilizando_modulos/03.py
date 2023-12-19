""" 
Seno, Cosseno e Tangente
Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
"""
from math import radians, sin, cos, tan

angulo = float(input("Digite um ângulo: "))

seno = sin(radians(angulo))

cosseno = cos(radians(angulo))

tangente = tan(radians(angulo))

print(f"O angulo {angulo}° apresenta: \nSENO de {seno:.2f} \nCOSSENO de {cosseno:.2f} \nTANGENTE de {tangente:.2f}")
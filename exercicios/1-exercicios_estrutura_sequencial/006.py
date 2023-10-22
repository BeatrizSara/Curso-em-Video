""" 
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
"""
import math

raio = float(input("Qual é o raio do circulo? "))

circunferencia = raio**2
area = math.pi * circunferencia

print("A area do circulo é: ", area)

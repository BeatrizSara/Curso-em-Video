""" 
Gerar um numero aleatório 
"""
import random

numero_aleatorio = random.randint(1, 100)

while True:
    numero_chute = int(input("Chute um número de 1 a 100: "))
    
    if numero_chute == numero_aleatorio:
        print("Vc acertou")
        break
        

print("Vc errou, tente novamente")

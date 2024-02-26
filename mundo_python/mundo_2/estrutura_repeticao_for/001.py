""" 
Exercicio 046
Contagem Regressiva
Faça um programa que msotre na tela uma contagem regressiva para o estouro de fogos de artificio,
indo de 10 até 0, com uma pausa de 1 ou 0.5 segundo entre eles. "Meio segundo - sleep(0.5)"
"""
from time import sleep

print("INICIANDO")
sleep(1)
print("CONTAGEM REGRESSIVA")
sleep(1)

for contagem in range(10, -1, -1):
    sleep(0.5)
    print(contagem)
sleep(1)
print("🎇  🎇  🎇 HAPPY NEW YEAR  🎇  🎇  🎇")
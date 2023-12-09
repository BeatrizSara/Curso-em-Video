""" 
Radar eletrônico 
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$ 7,00 por cada Km acima do limite.
"""

velocidade = float(input("Qual é a velocidade atual do carro? "))

if velocidade > 80:
    print("Multado! Excedeu o limite permitido de 80Km/h")
    multa = (velocidade - 80) * 7
    print(f"Voce deve pagar uma multa no valor de R$ {multa:.2f}")

print("Tenha um ótimo dia.\nDirija com cuidado!")
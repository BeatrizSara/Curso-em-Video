""" 
Custo de viagem 
Desenvolva um programa que pergunte a distancia de uma viagem em Km. 
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km 
e R$0,45 para viagens mais longas
"""

distancia =float(input("Informe qual a distancia da sua vigem: "))
print(f"Sua viagem de {distancia}Km logo vai iniciar.")

if distancia <= 200:
    custo_total = distancia * 0.50

else:
    custo_total = distancia * 0.45
    
print(f"O valor da passagem com a distancia de {distancia}Km, será de R${custo_total:.2f}")
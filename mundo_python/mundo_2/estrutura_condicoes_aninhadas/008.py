""" 
Indice de Massa Corporal - 043
Desenvolva uma lógica que leia o peso e a altura de uma pessoa,
calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
- Abaixo de 18.5: Abaixo do Peso
- Entre 18.5 e 25: Peso ideal
- 25 até 30: Sobrepeso
- 30 até 40: Obesidade
- Acima de 40: Obesidade mórbida
"""
print(str("---- CÁLCULO IMC ----" ))

peso = float(input("Informe seu peso:(Kg)"))
altura = float(input("Informe sua altura: (m)"))

imc = peso/(altura**2)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Abaixo do Peso normal")
#ou 18.5 <= imc < 25: (obs: python aceita essa forma)
elif imc <= 25:
    print("Peso normal")
    
elif imc <= 30:
    print("Sobrepeso")

elif imc <= 40:
    print("Obesidade")

else: 
    print("Obesidade Mórbida")
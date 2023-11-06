""" 
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder 
- positivamente a 2 questões ela deve ser classificada como "Suspeita", 
- entre 3 e 4 como "Cúmplice" e 
- 5 como "Assassino". 
Caso contrário, ele será classificado como "Inocente".
"""
print("Responda 'Sim' ou 'Não', para as seguintes perguntas:")

resposta1 = input("Telefonou para a vítima? ").lower()
resposta2 = input("Esteve no local do crime? ").lower()
resposta3 = input("Mora perto da vítima? ").lower()
resposta4 = input("Devia para a vítima? ").lower()
resposta5 = input("Já trabalhou com a vítima? ").lower()

respostaSim = 0

if resposta1 == "sim":
    respostaSim += 1
    
if resposta2 == "sim":
    respostaSim += 1
    
if resposta3 == "sim":
    respostaSim += 1

if resposta4 == "sim":
    respostaSim += 1

if resposta5 == "sim":
    respostaSim += 1


if respostaSim < 2:
    print("Inocente")

elif respostaSim < 3:
    print("Suspeito")

elif respostaSim < 5: 
    print("Cúmplice")

else:
    print("Assassino")

#Se RespostasSim é igual a 2 (Suspeito)
#Se Respostas Sim é igual a 3 ou 4 (Cúmplice)
#Se respostas sim é igual a 5 ( Assassino)
#Se - (Inocente)

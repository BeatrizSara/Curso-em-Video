""" 
Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO"
"""
cid = str(input("Qual cidade você nasceu? "))
print(cid[:5].upper() == "SANTO")
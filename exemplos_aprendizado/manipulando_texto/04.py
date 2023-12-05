""" 
Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
"""
# in - não é método. É um operador!

nome = str(input("Informe seu nome completo: ")).strip()
print(f"Seu nome tem Silva? {"SILVA" in nome.upper()}")
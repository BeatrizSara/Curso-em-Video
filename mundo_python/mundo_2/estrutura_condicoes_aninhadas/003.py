""" 
Comparando Números
Escreva um programa que leia dois números inteiros e compáre-os, mostrando na tela uma mensagem:
- O primeiro valor é maior
- O segundo valor é maior
- NÃO EXISTE valor maior, os dois são iguais
"""
num_1 = int(input("Informe o primeiro número inteiro: "))
num_2 = int(input("Informe o segundo número inteiro: "))

if num_1 > num_2:
    print(f"O primeiro número é maior")
elif num_1 < num_2:
    print(f"O segundo número é maior")
else:
    print(f"Os números {num_1} e {num_2} são iguais! Não existe valor maior")
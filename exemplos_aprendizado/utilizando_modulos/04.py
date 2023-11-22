""" 
Sorteando um item na lista
Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
"""
import random 

n1 = input("Informe um nome:")
n2 = input("Informe um segundo nome:")
n3 = input("Informe um terceiro nome:")
n4 = input("Informe um quarto nome:")

lista = [n1,n2,n3,n4]

escolhido = random.choice(lista)

print(f"O aluno escolhido foi: {escolhido}")
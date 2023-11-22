""" 
Sorteando uma ordem na lista 
O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia os nome dos quatro  alunos e mostre a ordem sorteada.
"""
from random import shuffle

n1 = input("Informe um nome:")
n2 = input("Informe um segundo nome:")
n3 = input("Informe um terceiro nome:")
n4 = input("Informe um quarto nome:")

lista = [n1,n2,n3,n4]
shuffle(lista)
print(f"A ordem de apresentação será:\n {lista}")
""" 
Primeiro e último nome de uma pessoa
Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
Ex: Ana Maria de Souza
primeiro = Ana
último = Souza

ESDRAS RAFAEL DA ROCHA
nome = ["ESDRAS", "RAFAEL", "DA", "ROCHA"] 
quantidadePalavras = len(nome)
print(nome[quantidadePalavras - 1])


"""
n = str(input("Informe seu nome completo: ")).strip()
nome = n.split()
print(f"Muito prazer em te conhecer!\nSeu primeiro nome é {nome[0]}\nSeu último nome é {nome[len(nome)-1]}")

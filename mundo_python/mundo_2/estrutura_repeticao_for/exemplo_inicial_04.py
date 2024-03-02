"""Exemplos simples de Estrutura de repetição FOR"""
n = int(input("Digite um número: "))
for c in range(0,n):
    print(c)
print("FIM")

#Utilizo o "n" como parte de passagem pro FOR
# Posso usar essa mesma linha de raciocinio

inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for c in range( inicio, fim+1, passo):
    print(c)
print("FIM")
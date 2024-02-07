""" 
Exercicio 049
Tabuada.2.0
Refaça o Desafio 009, mostrando a tabuada de um número que 
o usuário escolhe, só que agora utilizando um laço for 
"""
numero = int(input("Informe um número para verificar a TABUADA : "))

for tab in range(0, 11):
    print("{} x {} = {}".format(numero, tab, numero*tab))


""" 
Lacos de repetição usando FOR e WHILE - Exemplo
"""
#Exemplo 1

lista = [1, 2, 3, 4, 5]

for item in lista: # para cada item na lista
    print(item)

#Exemplo 2
nome = "ESDRAS"

for letra in nome: # Para cada letra no nome(palavra) - "Esdras"
    print(letra)
    
#Exemplo 3

lista_2 = [22, 23, 24, 25, 26] 

for numero in lista_2:
    if numero % 2 == 0: # quero testar para "cada"(item - numero) vai testar se é par ou impar
        print("O número {} é par". format(numero))
    else:
        print("O número {} é ímpar".format(numero))

#Exemplo 4
# Laço usando While

while True:
    print("Informe números, digite 0 para PARAR.")
    numero =  int(input("Informe um número:"))
    if numero == 0:
        print("ENCERRADO! Voce digitou 0!")
        break
    else:
        if numero % 2== 0:
            print("O número {} é PAR!".format(numero))
        else:
            print("O número {} é ÍMPAR!".format(numero))
            
""" 
GAME - Pedra, Papel e Tesoura - 045 
Vitoria - Empate - Derrota
Crie um programa que faça o computador jogar Jokenpô com você.
mundo 1 - utilizando modulos - utiliza random
o computador vai randomizar numero inteiro entre 0 e 2, pedra, papel, tesoura por isso item[computador]
Jo ken pô - com time de 1 segundo - importar biblioteca
"""

#Deve-se importar a classe Randon 
from random import randint
from time import sleep 

itens = ("PEDRA", "PAPEL", "TESOURA")
computador = randint(0,2)

print("""Suas opções:
    [0] PEDRA 🪨
    [1] PAPEL 📄
    [2] TESOURA ✂️""") 
jogador = int(input("Escolha a jogada: "))

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ!!!")
sleep(1)

print("-=" * 12)
print("O computador jogou {}".format(itens[computador]))
print("O jogador jogou {}".format(itens[jogador]))
print("-=" * 12)

if computador == 0:  
    if jogador == 0:
        print("EMPATOU!")
    elif jogador == 1:
        print("Jogador GANHOU!")
    elif jogador == 2:
        print("Computador GANHOU!")
    else:
        print("Jogada Inválida")
    
elif computador == 1:
    if jogador == 0:
        print("Computador GANHOU!")
    elif jogador == 1:
        print("EMPATOU!")       
    elif jogador == 2:
        print("Jogador GANHOU!")
    else:
        print("Jogada Inválida")
        
elif computador == 2:
    if jogador == 0:
        print("Jogador GANHOU!")
    elif jogador == 1:
        print("Computador GANHOU!")
    elif jogador == 2:
        print("EMPATOU!")
    else:
        print("Jogada Inválida")
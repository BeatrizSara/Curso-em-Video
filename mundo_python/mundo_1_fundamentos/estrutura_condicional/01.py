""" 
Jogo da Advinhação
Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 
e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. 
O pragrama deverá escrever na tela se o usuário venceu ou perdeu.
"""
from random import randint # de ramdom, gera números aleatórios, quero importar números aleatórios inteiros de 0 a 5.
computador = randint(0,5) # Faz o computador "pensar" \ Crio uma variável que receba randint com os números que desejo inserir no jogo

print("-=-" * 15)
print("  Vou pensar em um número inteiro de 0 a 5.")
print("-=-" * 15)

jogada = int(input("Em que número eu pensei? ")) # Jogador tenta advinhar

if jogada == computador:
    print(f"PARABÉNS! Você acertou!\nPensei no número {computador}")
    
else:
    print(f"Que pena. Voce perdeu.\nO número foi: {computador}. Tente novamente")
""" 
Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, 
se ele ainda vai se alistar ao serviço militar,
se já passou do tempo do alistamento. 
Seu programa também deverá mostrar :
o tempo que FALTA ou que PASSOU do prazo
"""
from datetime import date

atual = date.today().year
ano = int(input("Qual o ano de nascimento: "))
idade = atual - ano
print("Nascimento no ano {} tem {} anos".format(ano,idade,atual))

if idade == 18:
    print("Já possui a idade obrigatória para o alistamento")

elif idade < 18:
    saldo = 18 - idade 
    print(f"Ainda não possui a idade para se alistar. Falta {saldo} anos")

else:
    saldo = idade - 18
    print(f"Sua idade já passou da idade obrigatória para se alistar. Deveria ter se alistado a {saldo} anos")
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
print("Nascimento no ano {} tem {} anos").format(ano,idade,atual)

if idade == 18:
    print("Já possui a idade obrigatória para o alistamento")

elif idade < 18:
    print("Ainda não possui a idade para se alistar")
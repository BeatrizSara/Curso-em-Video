""" 
Alistamento Militar
Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade, 
se ele ainda vai se alistar ao serviço militar,
se já passou do tempo do alistamento. 
Seu programa também deverá mostrar :
o tempo que FALTA ou que PASSOU do prazo
O programa deve identificar se é Homem ou mulher - Masculino ou Feminino
"""
from datetime import date

atual = date.today().year
nascimento = int(input("Qual o ano de nascimento: "))
sexo = str(input("Feminino - F ou Masculino - M: ")).upper()
idade = atual - nascimento

print("Nascimento no ano {} tem {} anos".format(nascimento,idade,atual))
if sexo == "F":
    print("Você não precisa realizar o alistamento militar")

else:
    if idade == 18:
        print("Já possui a idade obrigatória para o alistamento")

    elif idade < 18:
        saldo = 18 - idade 
        ano_alistamento = atual + saldo
        print(f"Ainda não possui a idade para se alistar. Falta {saldo} anos")
        print(f"Seu alistamento será em {ano_alistamento}")

    else:
        saldo = idade - 18
        ano_alistamento = atual - saldo
        print(f"Sua idade já passou da idade obrigatória para se alistar. Deveria ter se alistado a {saldo} anos")
        print(f"Seu alistamento foi em {ano_alistamento}")

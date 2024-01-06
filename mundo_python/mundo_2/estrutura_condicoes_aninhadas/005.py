""" 
Classico da Média
Crie um programa que calcule as duas notas de um aluno e calcule sua média,
mostrando uma mensagem final, de acordo com a média atingida:
- Média abaixo de 5.0 : Reprovado
- Média entre 5.0 e 6.9 : Recuperação
- Média 7.0 ou superior: Aprovado
"""
n1 = float(input("Primeira nota:"))
n2 = float(input("Segunda nota:"))

s = (n1 + n2) / 2

print(f"Com as notas {n1} e {n2}, a média é {s:.1f}")

if s > 7.0:
    print(f"Sua nota foi {s:.1f}. APROVADO.")   
    
elif s >= 5.0:
    print(f"Sua nota foi {s:.1f}. RECUPERAÇÃO")

else:
    print(f"Infelizmente sua nota final foi {s:.1f}. REPROVADO")
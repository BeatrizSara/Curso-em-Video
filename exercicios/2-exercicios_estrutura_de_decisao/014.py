"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo:
  Média de Aproveitamento  Conceito
  Entre 4.0 e zero        E
  Entre 4.0 e 6.0         D
  Entre 6.0 e 7.5         C
  Entre 7.5 e 9.0         B
  Entre 9.0 e 10.0        A
"""
nota_primeiro_trimestre = float(input("Informe a nota do 1° trimestre: "))
nota_segundo_trimestre = float(input("Informe a nota do 2° trimestre: "))

mediaSemestre = (nota_primeiro_trimestre + nota_segundo_trimestre) / 2

if mediaSemestre < 4.0:
  print(f"Sua média é: {mediaSemestre:.2f}, Conceito E")
  
elif mediaSemestre < 6.0:
  print(f"Sua média é: {mediaSemestre:.2f}, Conceito D")

elif mediaSemestre < 7.5:
  print(f"Sua média é: {mediaSemestre:.2f}, Conceito C")

elif mediaSemestre < 9.0:
  print(f"Sua média é: {mediaSemestre:.2f}, Conceito B")

else:
  print(f"Sua média é: {mediaSemestre:.2f}, Conceito A")
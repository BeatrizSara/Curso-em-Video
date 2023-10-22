"""
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
"""
lado = float(input("Qual o valor do lado do quadrado? "))
area = lado**2
dobro = area*2

print(f"O lado de um quadrade de {lado: .2f}m tem uma area de {
      area: .2f}m² e o dobro da area tem {dobro: .2f}m²")

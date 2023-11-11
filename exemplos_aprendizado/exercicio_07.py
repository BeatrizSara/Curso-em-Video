""" 
Faça um programa que leia a largura e a altura de uma parede em metros.
Calcule a sua área e a quantidade de tinta necessária para pintá-la, 
Sabendo que cada litro de tinta pinta uma área de 2m**2
"""

altura = float(input("Informe a altura da parede: "))
largura = float(input("Informe a largura da parede: "))

litro = 2
area = largura * altura
quantidadeTinta = area / litro

print(f"Para pintar uma parede de {largura:.2f}m de largura e {altura:.2f}m de altura, será necessário {quantidadeTinta:.0f}L para pintá-la!")
""" 
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

# Pergunta sobre três produtos
produto1 = float(input("Informe o preço do primeiro produto: R$"))
produto2 = float(input("Informe o preço do segundo produto: R$"))
produto3 = float(input("Infome o preço do terceiro produto: R$"))

# Utiliza a função  min
produtoBarato = min(produto1, produto2, produto3)

# Informar qual produto você deve comprar ( decisão pelo produto mais barrato)
print(f"O produto que você deve comprar é no valor de: R$ {
      produtoBarato: .2f}")

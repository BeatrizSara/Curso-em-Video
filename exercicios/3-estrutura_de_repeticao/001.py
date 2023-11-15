""" 
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.
"""
while True:
    nota = float(input("Informe uma nota entre zero a dez: "))

    if 0 <= nota <= 10:
        break

    else:
        print("Valor não válido. A nota deve ser entre zero e dez.")

print(f"A nota informada foi: {nota}")
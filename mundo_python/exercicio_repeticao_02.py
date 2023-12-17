"""
    Faça um programa usando while que print a tabuada do número solicitado.
    Dicas:  Use while
            Use uma variavel que servira de contador e incrementara ela mesma a cada execução do while
"""

tabuada = int(input("Digite um numero para tabuada: "))

contador = 0

print(f"TABUADA DO NÚMERO {tabuada}")

while contador <=10:
    print(f"{contador} x {tabuada} = {contador * tabuada} ")
    contador += 1 
     


""" 
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
"""
letra = input("Informe uma letra: ").lower()

if len(letra) == 1:
    if letra in "aeiou":
        print("Vogal!")
    else:
        print("Consoante!")
else:
    print("Informe apenas uma letra.")

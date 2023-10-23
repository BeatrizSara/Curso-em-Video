"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""
# Upper() - faz com que toda string fique maiúscula

sexo = input("Informe F para Feminino ou M para Masculino: ").upper()


match sexo:
    case "M":
        print("Masculino")
    case "F":
        print("Feminino")
    case _:
        print("Sexo Inválido")

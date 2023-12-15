""" 
Outra forma de utilizar as cores com mensagens exibidas "Beatriz Sara"
"""

#Outra forma de utilizar as cores
nome = "Beatriz Sara"
cores = { "limpa" : "\033[m",
         "azul" : "\033[34m",
         "roxo" : "\033[7;45m",
         "pretoebranco" : "\033[7;37m"}


#Basicamente, isso é um dicionário de cores que pode utilizar para mudar a mensagem  exibida 
print("Olá! Muito prazer em te conhecer, {}{}{}!!".format(cores["roxo"], nome, cores["limpa"]))
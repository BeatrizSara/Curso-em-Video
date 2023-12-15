""" 
Boas Vindas com cores
"""
nome = "Beatriz Sara"

print(f"😊 Olá! Muito prazer em te conhecer, \033[4;35;40m{nome}\033[m \u2764")

#ou utilizar outra forma para exibir a mensagem
print("😊 Olá! Muito prazer em te conhecer, {}{}{}".format("\033[7;45m", nome,"\033[m \u2764"))


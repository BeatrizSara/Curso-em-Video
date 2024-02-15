while True:
    print("""######   #######    ##     ######   ######    ####    #######
 ##  ##   ##   #   ####    # ## #    ##  ##    ##     #   ##
 ##  ##   ## #    ##  ##     ##      ##  ##    ##        ##
 #####    ####    ##  ##     ##      #####     ##       ##
 ##  ##   ## #    ######     ##      ## ##     ##      ##
 ##  ##   ##   #  ##  ##     ##      ##  ##    ##     ##    #
######   #######  ##  ##    ####    #### ##   ####    #######""")
    break

import random
from colorama import init, Fore, Style

# Inicializa o colorama (apenas necessário no Windows)
init()

while True:
    # Gera uma cor RGB aleatória
    def cor_aleatoria():
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        return f'\033[38;2;{r};{g};{b}m'

    # Exemplo de uso com cor aleatória
    texto = 'BEATRIZ SARA!'
    cor = cor_aleatoria()

    print(cor + texto + Style.RESET_ALL)
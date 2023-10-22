""" 
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""
# 1 MB (megabyte) = 1.024 KB (kilobyte) = 1000000 byte

arquivo_download = float(
    input("Informe um tamanho de arquivo para download em MB: "))
velocidade_internet = float(
    input("Informe uma velocidade de um link de Internet em Mbps: "))

# Calcularr o tempo do download em minutos
# 1) Converter 1 byte = 8 bites
velocidade_internet = velocidade_internet / 8

# 2) Calcular o tempo e converter segundos para minutos
tempo_segundos = arquivo_download / velocidade_internet
tempo_minutos = tempo_segundos / 60


print(f"O tempo aproximado para download: {
      tempo_minutos: .0f} minutos e {tempo_segundos: .0f} segundos")

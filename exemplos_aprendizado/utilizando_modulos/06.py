""" 
Tocando um MP3
Faça um programa em Python que abra e reproduza o audio de um arquivo MP3.
"""

import pygame 
pygame.init() 
pygame.mixer.music.load("exer06.mp3")
pygame.mixer.music.play()
input("Aperte Enter para parar a música: ")
pygame.event.wait()
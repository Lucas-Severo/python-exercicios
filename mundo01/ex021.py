'''
Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
'''

# from playsound import playsound  # pip install playsound
# playsound('musica.mp3')

import pygame

musica = 'musica.mp3'

pygame.mixer.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()
input('\nENTER PARA FINALIZAR')
pygame.mixer.music.stop()

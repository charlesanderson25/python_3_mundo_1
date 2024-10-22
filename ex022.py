#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame

pygame.mixer.init() #inicia o pygame

pygame.mixer.music.load('Nome do arquivo') #lê arquivo MP3

pygame.mixer.music.play() #reproduz o arquivo MP3

pygame.event.wait()
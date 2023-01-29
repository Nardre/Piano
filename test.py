#!/bin/python3
import pygame
from pygame.locals import *

# initialisation
height, width = 383, 1150

# fenetre
pygame.init()
fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption('piano')

# boucle infini
continuer = True
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = False

        # keyboard
        if event.type == KEYDOWN:
            print(event.key)

# quit
pygame.quit()



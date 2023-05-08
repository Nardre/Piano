#!/bin/python3
import pygame
from pygame.locals import *
from touche import *
from monotome import *
from partition import *

# initialisation
width, height = 1828, 1020
#width, height = 1228, 1020

# fenetre
pygame.init()
fenetre = pygame.display.set_mode((width, height))
pygame.display.set_caption('piano')

partition = Partition(fenetre)

# touche
blanche = ["blanche.xcf", "blanche1.xcf"]
dimbl = (62, 354)
noire = ["noire.xcf", "noire1.xcf"]
dimno = (38, 209)

touches = []
for i in range(29):
    lettre = "cdefgab"[i%7]
    numero = i//7 + 2
    touches += [Touche(fenetre, blanche, f"{numero}-{lettre}.wav", dimbl, (i*63, 0))]

for i in range(28):
    if i%7!=2 and i%7!=6:
        lettre = ["cs", "ds", " ", "fs", "gs", "as", " "][i%7]
        numero = i//7 + 2
        position = (63*i+45, 0)
        touches += [Touche(fenetre, noire, f"{numero}-{lettre}.wav", dimno, position)]    


#auto
AUTOFPS = USEREVENT + 1
pygame.time.set_timer(AUTOFPS, 16)

# boucle infini
continuer = True
while continuer:
    for event in pygame.event.get():    
        if event.type == QUIT:
            continuer = False 

        if event.type == AUTOFPS:
            for touche in touches:
                touche.affichage()
            partition.affichage()
            pygame.display.flip()
        
        #souris
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            i = len(touches)-1
            while i>=0 and not touches[i].play(event.pos):
                i-=1
            if partition.get_i() == 29-i-1:
                pygame.draw.rect(fenetre, (0, 255, 0), [0, 332, 1828, 1788])
            else:
                pygame.draw.rect(fenetre, (255, 0, 0), [0, 332, 1828, 1788])
            partition.play()

        # keyboard
        if event.type == KEYDOWN :
            partition.play()

# quit
pygame.quit()


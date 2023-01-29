import pygame
from pygame.locals import *
import random

class Partition:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.partition = pygame.image.load("images/partition1.xcf").convert_alpha()
        self.ronde = pygame.image.load("images/ronde.xcf").convert_alpha()
        self.ronde = pygame.transform.scale(self.ronde, (52, 30))
        self.i = 0
        
    def affichage(self):
        self.fenetre.blit(self.partition, (332, 380))
        self.fenetre.blit(self.ronde, (889, 421+self.i*19 + self.i//14*10))
    
    def play(self):
        self.i = random.randrange(29)
    
    def get_i(self):
        return self.i 

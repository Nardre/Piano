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
        self.x = 0
        self.last = 0
        self.lastx = 0
        self.font = pygame.font.SysFont('mono', 25)
        self.noteList = ["do", "re", "mi", "fa", "sol", "la", "si"][::-1]
        self.text = ""
        self.total = 0
        
    def affichage(self):
        self.fenetre.blit(self.partition, (432, 380))
        self.fenetre.blit(self.ronde, (689, 421+self.i*19 + self.i//14*10))
        self.fenetre.blit(self.ronde, (689, 421+self.x*19 + self.x//14*10))

        self.text = self.font.render(self.noteList[(self.last-1)%7], True, (0,0,0))
        self.fenetre.blit(self.text, (689, 700))
        
        self.text = self.font.render(str(self.total), True, (0,0,0))
        self.fenetre.blit(self.text, (639, 700))
    
        self.text = self.font.render(str(self.last - self.lastx), True, (0,0,0))
        self.fenetre.blit(self.text, (739, 700))

    def play(self):
        self.last = self.i
        self.lastx = self.x
        self.i = random.randrange(29)
        self.x = max(0, self.i - random.randint(2, 8))
        self.total += 1
        #self.i = random.randrange(16)
    
    def get_i(self):
        return self.i 

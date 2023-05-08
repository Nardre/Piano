import pygame
from pygame.locals import *
import time

class Monotome:
    def __init__(self, fenetre):
        self.fenetre = fenetre
        self.time = time.time()
        self.font = pygame.font.SysFont('mono', 25)
        self.duree = 0
        self.color = (0, 255, 0)
        self.start = time.time()

    def affichage(self):
        self.text = self.font.render(f"{self.duree}", True, self.color)
        self.fenetre.blit(self.text, (0, 25))

        text = int(time.time()-self.start)
        self.text = self.font.render(f"{text}", True, (0, 0, 0))
        self.fenetre.blit(self.text, (0, 0))
        
        pygame.draw.rect(self.fenetre, self.color, [0, 383, 1150, 100])

    def play(self):
        self.duree = round(time.time() - self.time, 2)
        #b = self.duree%0.75 <= 0.15 or self.duree%0.75 >= 0.6
        b = self.duree%1 <= 0.15 or self.duree%1 >= 0.85
        self.color = (0, 255, 0) if b else (255, 0, 0)
        self.time = time.time()

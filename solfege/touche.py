import pygame
from pygame.locals import *

class Touche:
    def __init__(self, fenetre, image, son, dim, pos):
        self.fenetre = fenetre
        self.image = []
        self.image.append(pygame.image.load("images/"+image[0]).convert())
        self.image.append(pygame.image.load("images/"+image[1]).convert())
        self.son = pygame.mixer.Sound("piano-88-notes/"+son)
        self.son.set_volume(0.25)
        self.dim = dim
        self.pos = pos
        self.press = False
        
        self.font = pygame.font.SysFont('mono', 25)
        self.text = self.font.render(f" do  re   mi  fa sol  la  si  do  re   mi  fa  sol la   si  do  re  mi  fa  sol  la  si  do  re   mi  fa sol  la  si  do", True, (0, 0, 0))

    def affichage(self):
        if not self.press:
            self.fenetre.blit(self.image[0], self.pos)
        else:
            self.fenetre.blit(self.image[1], self.pos)
            self.press = False
        #self.fenetre.blit(self.text, (0, 300))
    
    def play(self, pos):
        if self.pos[0]<=pos[0]<=self.pos[0]+self.dim[0] and \
           self.pos[1]<=pos[1]<=self.pos[1]+self.dim[1]:
            self.press = True
            self.son.play()
            self.son.fadeout(2000)
            return True
        return False


        

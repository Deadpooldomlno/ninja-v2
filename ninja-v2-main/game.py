from player import Player
from ennemy import Ennemy
#from background import Background
import pygame
pygame.init()

class Game:
    
    def __init__(self,screen):
        self.screen=screen
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.gravite = 0.5
        self.vitesse_max_chute = 12

        #self.bg = Background(self)       
        
        self.player = Player(self)
        self.ennemy = Ennemy(self,50,1)
    
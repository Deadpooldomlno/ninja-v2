from player import Player
from ennemy import Ennemy
import pygame
pygame.init()

class Game:
    
    def __init__(self,screen):
        self.screen=screen
        self.w = screen.get_width()
        self.h = screen.get_height()
        self.gravite = 0.5
        self.vitesse_max_chute = 12      
        
        self.nb_mort =0
        
        self.player = Player(self)
        self.ennemy = Ennemy(self,50,1)
        self.plateformes = [pygame.Rect(200, 500, 400, 20),pygame.Rect(100, 400, 200, 20),pygame.Rect(520, 325, 200, 20)]
   
        self.ennemies = []
        self.ennemies.append(self.ennemy.rect)
        self.players=[]
        self.players.append(self.player.rect)

    def reset(self):
        self.player = Player(self)
        self.ennemy = Ennemy(self,50,1)
        self.plateformes = [pygame.Rect(200, 510, 400, 20),pygame.Rect(100, 410, 200, 20),pygame.Rect(520, 335, 200, 20)]
   
        self.ennemies = []
        self.ennemies.append(self.ennemy.rect)
        self.players=[]
        self.players.append(self.player.rect)
        
        
        
    

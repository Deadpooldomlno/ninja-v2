from button import *
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
        
        #boutons
        self.button_setting = Button(screen,('assets/buttons/setting1.png','assets/buttons/setting2.png'),(self.w-30,20))
        self.button_restart = Button(screen,('assets/buttons/restart1.png','assets/buttons/restart2.png'),(self.w-66,20))
        self.button_play = Button(screen,('assets/buttons/play1.png','assets/buttons/play2.png'),(self.w/2,self.h/2),True)
        self.button_menu = Button(screen,('assets/buttons/menu1.png','assets/buttons/menu2.png'),(self.w/2,self.h/2-90),True)
        self.button_quit = Button(screen,('assets/buttons/exit1.png','assets/buttons/exit2.png'),(self.w/2,self.h/2+90),True)
        
        #textes
        self.death = Texte(screen,'assets/death.png',(57,20),True)
        self.timer = Texte(screen,'assets/timer.png',(355,20),True)
        self.bestTime = Texte(screen,'assets/bestTime.png',(85,20),True)

    #desine une bande grise
    def bande_grise(self):
        surf = pygame.Surface((self.w,40))
        surf.fill((127,127,127))
        surf_rect=surf.get_rect()
        self.screen.blit(surf,surf_rect)
    
    #reinitialise certins atributs
    def reset(self):
        self.player = Player(self)
        self.ennemy = Ennemy(self,50,1)
        self.plateformes = [pygame.Rect(200, 510, 400, 20),pygame.Rect(100, 410, 200, 20),pygame.Rect(520, 335, 200, 20)]
   
        self.ennemies = []
        self.ennemies.append(self.ennemy.rect)
        self.players=[]
        self.players.append(self.player.rect)
        

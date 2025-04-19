import pygame
pygame.init()
from random import randint

class Ennemy:
    
    def __init__(self,game,r,v):
        self.game = game
        self.surf = pygame.Surface((40,40))
        self.surf.fill((255,0,0))
        self.rect = self.surf.get_rect(center=(450,self.game.h/2))
        
        self.direction = 1
        self.vitesse_deplacement = v
        self.range = r
        
        self.vx = 0 
        self.vy = 0
        
        self.start_x = self.rect.x

    def degat(self):
        pass
    
    def deplacer_gauche(self):
        self.vx = -self.vitesse_deplacement 
        
    def deplacer_droite(self):
        self.vx = self.vitesse_deplacement 
    
    def update(self,plateformes,players):
        self.vy += self.game.gravite
        self.vy = min(self.vy, self.game.vitesse_max_chute)
        """
        self.vx += self.direction * self.vitesse_deplacement
        if abs(self.rect.x - self.start_x) >= self.range:
            self.direction *= -1
        """
        self.rect.x += self.vx
        
        #detection horizontale ennemi - plateforme
        for plateforme in plateformes:
            if self.rect.colliderect(plateforme):
                if self.vx > 0:
                    self.rect.right = plateforme.left
                    self.deplacer_gauche()
                elif self.vx < 0:  
                    self.rect.left = plateforme.right
                    self.deplacer_droite()
        
        if self.rect.left < 0:
            self.rect.left = 0
            self.deplacer_droite()
        elif self.rect.right > self.game.w:
            self.rect.right = self.game.w
            self.deplacer_gauche()
        
        self.rect.y += self.vy
        
        rect_test = self.rect.copy()
        rect_test.y += 1
        
        #detection verticale ennemi - plateforme
        for plateforme in plateformes:
            if self.rect.colliderect(plateforme) or rect_test.colliderect(plateforme):
                if self.vy > 0: 
                    self.rect.bottom = plateforme.top
                    self.vy = 0 
                elif self.vy < 0: 
                    self.rect.top = plateforme.bottom
                    self.vy = self.game.gravite +2
        
        if self.rect.bottom +1 > self.game.h:
            self.rect.bottom = self.game.h
            self.vy = 0             
        elif self.rect.top < 0:
            self.rect.top = 0
            self.vy = self.game.gravite +2
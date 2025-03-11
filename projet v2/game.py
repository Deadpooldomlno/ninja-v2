from player import Player
import pygame
pygame.init()

class Game:
    
    def __init__(self):
        self.w = 1000
        self.h = 600
        
        self.player = Player(self)
    
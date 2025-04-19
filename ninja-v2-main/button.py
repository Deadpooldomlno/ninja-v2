import pygame
pygame.init()

class Button:
    
    def __init__(self,screen,images,pos):
        self.screen=screen
        self.image1=pygame.image.load(images[0])
        self.image2=pygame.image.load(images[1])
        
        self.pos = pos
        
        self.current_image = self.image1
        self.rect = self.current_image.get_rect(center=pos)
        self.pressed = False
        
    def draw(self):
        if self.pressed:
            self.current_image = self.image2
        else:
            self.current_image = self.image1
        self.screen.blit(self.current_image,self.rect)
    
    def check_collision(self,mouse_pos):
        return self.rect.collidepoint(mouse_pos)
            
                
        
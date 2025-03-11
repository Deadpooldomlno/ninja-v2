from game import Game
import pygame
pygame.init()

plateformes = [
    pygame.Rect(200, 500, 400, 20),
    pygame.Rect(100, 400, 200, 20),
    pygame.Rect(500, 300, 200, 20),
    pygame.Rect(50, 100, 100, 20)
]

game = Game()

screen = pygame.display.set_mode((game.w, game.h))
pygame.display.set_caption('ninja v2')

fps= pygame.time.Clock()

running = True
while running :
    fps.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game.player.sauter()
            
    k = pygame.key.get_pressed()

    if k[pygame.K_LEFT]:
        game.player.deplacer_gauche()
    elif k[pygame.K_RIGHT]:
        game.player.deplacer_droite()
    else:
        game.player.arreter()
    
    screen.fill((255,255,255))
    screen.blit(game.player.surf, game.player.rect)
    game.player.update(plateformes)
    
    for plateforme in plateformes:
        pygame.draw.rect(screen, (0,0,0), plateforme)
    
    pygame.display.update()
pygame.quit()
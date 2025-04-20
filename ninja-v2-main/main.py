from button import Button
from game import Game
import pygame
pygame.init()

w,h=1000,600
screen = pygame.display.set_mode((w, h))
pygame.display.set_caption('ninja')

game = Game(screen)

button_setting = Button(screen,('assets/buttons/setting1.png','assets/buttons/setting2.png'),(w-30,20))
button_restart = Button(screen,('assets/buttons/restart1.png','assets/buttons/restart2.png'),(w-66,20))
button_play = Button(screen,('assets/buttons/play1.png','assets/buttons/play2.png'),(w/2,h/2),True)
button_menu = Button(screen,('assets/buttons/menu1.png','assets/buttons/menu2.png'),(w/2,h/2-90),True)
button_quit = Button(screen,('assets/buttons/exit1.png','assets/buttons/exit2.png'),(w/2,h/2+90),True)

surf = pygame.Surface((game.w,40))
surf.fill((127,127,127))
surf_rect=surf.get_rect()

fps= pygame.time.Clock()

#main
def main():
    state = 'menu'
    
    while state != 'quit':
        if state == 'play':
            state = play()
        elif state == 'setting':
            state = setting()
        elif state == 'menu':
            state = menu()
        elif state == 'restart':
            game.reset()
            state = 'play'

    pygame.quit()

#jeu
def play():    
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    game.player.sauter()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if button_setting.check_collision(mouse_pos):
                        return 'setting'
                    if button_restart.check_collision(mouse_pos):
                        game.nb_mort +=1
                        return 'restart'
                
        k = pygame.key.get_pressed()
        
        if k[pygame.K_LEFT] and k[pygame.K_RIGHT]:
            game.player.arreter()
        if k[pygame.K_LEFT]:
            game.player.deplacer_gauche()
        elif k[pygame.K_RIGHT]:
            game.player.deplacer_droite()
        else:
            game.player.arreter()
        
        screen.fill((255,255,255))
        screen.blit(game.player.current_image, game.player.rect)
        game.player.update()
        
        screen.blit(game.ennemy.surf, game.ennemy.rect)
        game.ennemy.update(game.plateformes, game.players)

        for plateforme in game.plateformes:
            pygame.draw.rect(screen, (0,0,0), plateforme)
        
        screen.blit(surf,surf_rect)
        for button in [button_setting,button_restart]:
            button.draw()
        
        pygame.display.update()

#options  
def setting():
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if button_quit.check_collision(mouse_pos):
                        return 'quit'
                    if button_menu.check_collision(mouse_pos):
                        return 'menu'
                    if button_play.check_collision(mouse_pos):
                        return 'play'
        
        screen.fill((255,255,255))
        screen.blit(surf,surf_rect)
        for button in [button_play,button_menu,button_quit]:
            button.draw()
        
        pygame.display.update()
#menu      
def menu():
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button ==1:
                    if button_play.check_collision(mouse_pos):
                        return 'restart'
                    if button_setting.check_collision(mouse_pos):
                        return 'setting'
        
        screen.fill((255,255,255))
        screen.blit(surf,surf_rect)
        for button in [button_play,button_setting]:
            button.draw()
        
        pygame.display.update()

main()

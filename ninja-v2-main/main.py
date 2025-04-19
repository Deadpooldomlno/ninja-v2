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
button_play = Button(screen,('assets/buttons/play1.png','assets/buttons/play2.png'),(w/2,h/2))
button_menu = Button(screen,('assets/buttons/menu1.png','assets/buttons/menu2.png'),(w/2,h/2+36))
button_quit = Button(screen,('assets/buttons/exit1.png','assets/buttons/exit2.png'),(w/2,h/2+72))

surf = pygame.Surface((game.w,40))
surf.fill((127,127,127))
surf_rect=surf.get_rect()

fps= pygame.time.Clock()

def main():
    state = 'setting'
    
    while state != 'quit':
        if state == 'play':
            state = play()
        elif state == 'setting':
            state = setting()
        elif state == 'menu':
            menu()
        #elif state == 'restart':
            
            
    print(state)

    pygame.quit()

def play():    
    plateformes = [pygame.Rect(200, 500, 400, 20),pygame.Rect(100, 400, 200, 20),pygame.Rect(520, 325, 200, 20)]
    
    ennemies = []
    ennemies.append(game.ennemy.rect)
    players=[]
    players.append(game.player.rect)
    
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
                if button_setting.check_collision(mouse_pos):
                    return 'setting'
                if button_restart.check_collision(mouse_pos):
                    print('restart')
                
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
        game.player.update(plateformes,ennemies)
        
        screen.blit(game.ennemy.surf, game.ennemy.rect)
        game.ennemy.update(plateformes, players)

        for plateforme in plateformes:
            pygame.draw.rect(screen, (0,0,0), plateforme)
        
        screen.blit(surf,surf_rect)
        for button in [button_setting,button_restart]:
            button.draw()
        
        pygame.display.update()
    
def setting():
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
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
        
def menu():
    while True :
        fps.tick(60)
        
        mouse_pos = pygame.mouse.get_pos()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_play.check_collision(mouse_pos):
                    return 'play'
                if button_setting.check_collision(mouse_pos):
                    return 'setting'
        
        screen.fill((255,255,255))
        screen.blit(surf,surf_rect)
        for button in [button_play,button_setting]:
            button.draw()
        
        pygame.display.update()

main()
import pygame
from sys import exit
import random as r

def main():
    pygame.init()

    width = 800
    height = 720

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Space Invaders')

    clock = pygame.time.Clock()
    running = True

    spaceSurface = pygame.image.load('background-blue.png')
    spaceSurface = pygame.transform.scale(spaceSurface, (width, height))
    
    planetSurface = pygame.image.load('sprites\spacepixels-0.2.0\planets\planet5.png')
    planetSurface = pygame.transform.scale(planetSurface, (width*.15, height*.15))
    
    player = pygame.image.load('sprites\space_pixels_ships_stroked\ship_green_stroked.png')

    xPlanet = r.randrange(0,width)*.9
    yPlanet = height*.1
    
    # if the game is still running, don't close it, but if we close the terminal, then quit the game
    while running:
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
                exit()
                
        #background color is black
        screen.blit(spaceSurface,(0,0))
        screen.blit(planetSurface, (xPlanet,yPlanet))
        screen.blit(player,(width/2, height-100))
        
        if not yPlanet > height:
            yPlanet += 0.3
        else:
            xPlanet = r.randrange(0,width)*.9
            yPlanet = -100
        
        #TODO RENDER GAME HERE
        
        #draw and update everything
        pygame.display.update()
        
        # framerate is 60 fps
        clock.tick(60)
        
    pygame.quit()
    
if __name__ == '__main__': main()
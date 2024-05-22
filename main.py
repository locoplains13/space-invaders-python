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
    testFont = pygame.font.Font('font\Pixeled.ttf', 18)
    score = 0

    spaceSurface = pygame.image.load('background-blue.png').convert_alpha()
    spaceSurface = pygame.transform.scale(spaceSurface, (width, height))
    
    planetSurface = pygame.image.load('sprites\spacepixels-0.2.0\planets\planet5.png').convert_alpha()
    planetSurface = pygame.transform.scale(planetSurface, (width*.15, height*.15))
    planetRect = planetSurface.get_rect()
    
    playerSurface = pygame.image.load('sprites\space_pixels_ships_stroked\ship_green_stroked.png').convert_alpha()
    playerSurface = pygame.transform.scale(playerSurface, (100,100))
    playerRect = playerSurface.get_rect(midbottom = (350,720))
    
    textSurface = testFont.render("Score: "+str(score), False, "White")
    
    projectileSurface = pygame.image.load('sprites\spacepixels-0.1.0\pixel_laser_blue.png').convert_alpha()
    projectileRect = projectileSurface.get_rect(center = (playerRect.x, playerRect.y))
    
    enemySurface = pygame.image.load('sprites\spacepixels-0.2.0\pixel_station_green.png').convert_alpha()
    enemyRect = enemySurface.get_rect()
        
    planetRect.right = r.randrange(0,width)
    
    # list of projectiles on screen
    projectiles = []
    enemies = []
    
    def add_enemy():
        new_enemy = enemySurface.get_rect(center=(r.randrange(0, width), -50))
        enemies.append(new_enemy)
    
    def move_projectiles():
        for projectile in projectiles:
            projectile.y -= 50
            if projectile.y < 0:
                projectiles.remove(projectile)
            else:
                screen.blit(projectileSurface, projectile)
    
    def move_enemies():
        direction = 2
        nonlocal score
        for enemy in enemies:
            enemy.x += direction
            if enemy.x > width:
                enemies.remove(enemy)
            if any(enemy.colliderect(projectile) for projectile in projectiles):
                enemies.remove(enemy)
                score += 1
            else:
                screen.blit(enemySurface, enemy)
            
    
    add_enemy()
    
    # if the game is still running, don't close it, but if we close the terminal, then quit the game
    while running:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                quit()
                
        # background color is black
        # declaring also every other surface on the display
        screen.blit(spaceSurface,(0,0))
        screen.blit(planetSurface, planetRect)
        screen.blit(playerSurface,playerRect)
        screen.blit(textSurface,(30,height-50))
        screen.blit(enemySurface,enemyRect)                           

        
        # resetting the planet sprite to reappear at random points outside the screen
        if not planetRect.top > height:
            planetRect.y += 1
        else:
            planetRect.x = r.randrange(0,width)*.9
            planetRect.y = -100
        
        # generates a fucking projectile, fuck this code    

        enemies.append(enemyRect)
        keys = pygame.key.get_pressed()
        
        # if certain keys are pressed then move the player in that direction,
        # do it this method, otherwise there'd be no continous movement       
        if keys[pygame.K_a]:
            playerRect.x -= 5
        if keys[pygame.K_d]:
            playerRect.x += 5
        if keys[pygame.K_w]:
            playerRect.y -= 5
        if keys[pygame.K_s]:
            playerRect.y += 5
        if keys[pygame.K_SPACE]:
            projectileRect = projectileSurface.get_rect(center = (playerRect.x, playerRect.y))
            if(len(projectiles) < 1):
                projectiles.append(projectileRect)            
        
        move_projectiles()
        move_enemies()
        
        if r.random() < 0.02:
            add_enemy()
        #draw and update everything
        pygame.display.update()
        
        # framerate is 60 fps
        clock.tick(60)
        
        
    pygame.quit()
    
if __name__ == '__main__': main()
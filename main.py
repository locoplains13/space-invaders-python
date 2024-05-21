import pygame

pygame.init()

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            running = False
            
    screen.fill("black")
    
    #TODO RENDER GAME HERE
    
    
    pygame.display.flip()
    
    clock.tick(60)
    
pygame.quit()
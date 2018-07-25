#Blake Finizio
#7/2/18
#First ever pygame

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pygame
#Initialize pygame
pygame.init()

white = [255,255,255]
red= [255,0,0]
                                    #Width  Height 
#Game display                        #  |   |    
gameDisplay = pygame.display.set_mode((500,400))
pygame.display.set_caption("Cubes")
clock = pygame.time.Clock() 
gameExit = False
leadX = 250
leadY = 200

leadXChange = 0
leadYChange = 0
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadXChange = leadXChange - 15
            if event.key == pygame.K_RIGHT:
                leadXChange = leadXChange + 15
            if event.key == pygame.K_UP:
                leadYChange = leadYChange - 15
            if event.key ==  pygame.K_DOWN:
                leadYChange = leadYChange + 15
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                leadYChange = 0
            elif  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                leadXChange = 0

    leadX = leadX + leadXChange
    leadY = leadY + leadYChange

    if leadX < 0 or leadX>500 or leadY <0 or leadY>400:
        gameExit = True
                        
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, [leadX,leadY,15,15])
    pygame.display.update()
    # specify fps
    clock.tick(10)

#Un-Initializes Pygame
pygame.quit()
quit()

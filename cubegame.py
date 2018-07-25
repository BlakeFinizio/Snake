#Blake Finizio
#7/2/18
#First ever pygame

#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
import pygame
#Initialize pygame
pygame.init()

white = [255,255,255]
red= [255,0,0]

width = 700
height = 600                              #Width  Height 
#Game display                        #  |   |    
gameDisplay = pygame.display.set_mode((width,height))
pygame.display.set_caption("Cubes")
clock = pygame.time.Clock() 
gameExit = False
leadX = width / 2
leadY = height / 2
cubeSizeX = 15
cubeSizeY = 15
FPS = 10
leadXChange = 0
leadYChange = 0
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leadXChange = leadXChange - cubeSizeX
            if event.key == pygame.K_RIGHT:
                leadXChange = leadXChange + cubeSizeX
            if event.key == pygame.K_UP:
                leadYChange = leadYChange - cubeSizeY
            if event.key ==  pygame.K_DOWN:
                leadYChange = leadYChange + cubeSizeY
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                leadYChange = 0
            elif  event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                leadXChange = 0

    leadX = leadX + leadXChange
    leadY = leadY + leadYChange

    if leadX < 0 or leadX>width or leadY <0 or leadY>height:
        gameExit = True
                        
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, [leadX,leadY,cubeSizeX,cubeSizeY])
    pygame.display.update()
    # specify fps
    clock.tick(FPS)

#Un-Initializes Pygame
pygame.quit()
quit()

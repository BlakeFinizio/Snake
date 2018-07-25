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

gameExit = False
while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, [205xc0,200,15,15])
    pygame.display.update()
















#Un-Initializes Pygame
pygame.quit()
quit()

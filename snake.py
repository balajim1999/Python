###SNAKE GAME

#create the screen
import pygame
pygame.init()
dis=pygame.display.set_mode((800,600))
pygame.display.update()
pygame.display.set_caption('SNAKE GAME')

#hold the screen
Game_Over = False
while not Game_Over:
    for event in pygame.event.get():

#quit the screen by using X user interface
        if event.type==pygame.QUIT:
            Game_Over=True
pygame.quit()
quit()




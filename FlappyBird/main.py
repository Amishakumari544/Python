# generating random numbers
import random
import sys #used for closing the file or exit the game
import pygame
from pygame.locals import * #basic pygame imports

# /gloabal Variables for the game 
FPS=32 #Fps = frame per second for the image how many frames rendering in one second
SCREENWIDTH=300
SCREENHEIGHT=500
# Making screen
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT)) #initialize a window for display
GROUNDY     #this is used for ground image size that how much does it takes space for ground
GAME_SPRITES={} #used for moving the 2d game
GAME_SOUNDS ={}
PLAYER=''
BACKGROUND='/gallery/background.jpg'
PIPE=''
if __name__ == '__main__': #run from this main
    pygame.init() #initialize pygame modules
    FPSCLOCK=pygame.time.Clock() #used to control the fps by creating object
    pygame.display.set_caption("Flappy Game by Amisha")
    GAME_SPRITES['numbers']=(
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
        pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
    )
    GAME_SPRITES['messages'] = pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
    GAME_SPRITES['base'] = pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
    GAME_SPRITES['pipe'] = pygame.image.load('').convert_alpha #convert alpha and convert is different to make smooth functioning
    # to rotate the pipe
    pygame.transform.rotate()(pygame.image.load(PIPE).convert_alpha(),180)
    pygame.image.load(PIPE).convert_alpha()
    )


    # Game Sounds to add
    GAME_SOUNDS['die'] = pygame.mixer.Sound('')
    GAME_SOUNDS['hit'] = pygame.mixer.Sound('')
    GAME_SOUNDS['point'] = pygame.mixer.Sound('')
    GAME_SOUNDS['swoosh'] = pygame.mixer.Sound('')
    GAME_SOUNDS['wing'] = pygame.mixer.Sound('')

    GAME_SPRITES['background']=pygame.image.load(BACKGROUND)convert()
    GAME_SPRITES['player']=pygame.image.load(PLAYER)convert_alpha() #helps to change image with pixels

    while True:
        welcomeScreen() #shows welcome screen  to the user until he press any button
        mainGame()  #starts playing the game from this function
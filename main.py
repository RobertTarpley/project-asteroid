# this allows us to use code from the open-source pygame library throughout this file
import pygame
from constants import *

def main():
    pygame.init()
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    clock = pygame.time.Clock()
    dt = 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return #exit the main function
        
        #fill the screen with black
        screen.fill((0, 0, 0))
        
        #refresh the display
        pygame.display.flip()
        
        #cap the frame rate at 60 fps and set dt 
        dt = clock.tick(60) / 1000
        

if __name__ == "__main__":
    main()

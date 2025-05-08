#allows us to use code from pygame library
import pygame
from constants import *
from player import Player

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
clock = pygame.time.Clock()

#delta time, setted below


def main():
    
    dt = 0
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2

    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(x,y)
  #game-loop:
    while True:

        #close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)
        
        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #set framerate to 60
        dt = clock.tick(60)/1000
        print(dt)

if __name__ == "__main__":
    main()

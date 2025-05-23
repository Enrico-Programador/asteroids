#allows us to use code from pygame library
import sys
import pygame
from asteroid import Asteroid
from constants import *
from player import Player
from shot import Shot
from asteroidfield import AsteroidField
from gamestate import GameState

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
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)
    GameState.containers = (updatable)

    player = Player(x,y)
    asteroidfield = AsteroidField()
    gamestate = GameState()
  #game-loop:
    while True:

        #close the game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        pygame.Surface.fill(screen, (0,0,0))
        updatable.update(dt)

        for asteroid in asteroids:
            gameover = asteroid.colision(player)
            if gameover == True:
                print("GAME OVER!!!")
                sys.exit()

        for asteroid in asteroids:
            for shot in shots:
                collision = asteroid.colision(shot)
                if collision == True:
                    gamestate.pointcounter()
                    asteroid.split()
                    shot.kill()

                    if gamestate.difficulty_counter >= 1:  #this increases dificulty every 50 points
                        asteroidfield.speed_multiplier *= 1.2 #increase speed of all future asteroids
                        gamestate.difficulty_counter = 0 #reset the counter to update every 50 points
                        for asteroid in asteroids:  #increases speed of all existing asteroids
                            asteroid.velocity *= 1.2
                    break


        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        #set framerate to 60
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()

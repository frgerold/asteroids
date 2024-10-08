# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    clock = pygame.time.Clock()
    dt = 0
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    Asteroid.containers = (updatable, drawable, asteroids)
    AsteroidField.containers = (updatable)
    Shot.containers = (updatable, drawable, shots)
    asteroidfield = AsteroidField()
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)



    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(pygame.Color(0, 0, 0))
        for object in updatable:
            object.update(dt)
        for object in asteroids:
            if object.collide(player):
                exit("Game over!")
        for asteroid in asteroids:
            for bullet in shots:
                if bullet.collide(asteroid):
                    asteroid.split()
                    bullet.kill()
        for object in drawable:
            object.draw(screen)

                

        #player.draw(screen)
        #player.update(dt)
        pygame.display.flip()
        #print(f"{len(asteroids)}")
        dt = clock.tick(60)/1000
        

if __name__ == "__main__":
    main()
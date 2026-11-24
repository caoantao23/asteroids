import pygame   
from constants import *
from logger import log_state
from player import *

def main():
    pygame.init() 
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}") 

    clock = pygame.time.Clock()
    dt = 0.0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)
    player1 = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT /2)        

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return         
        dt = clock.tick(60) / 1000
        for sprite in updatable:
            updatable.update(dt)
        # player1.update(dt)

        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)        
        # player1.draw(screen)
        
        pygame.display.flip()
         
          

      

if __name__ == "__main__":
    main()

import pygame # type: ignore

from constants import *

def main():
    print("Starting Asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)

    running = True
    paused = False

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_p:
                paused = not paused #toggles pause when "P" is pressed
                if paused:
                    print("GAME PAUSED")
                    continue
                else:
                    print("GAME UNPAUSED")
                    continue
            #TODO assign more control

        #Pause handling
        if paused:
            screen.fill((20, 20, 40))
            pygame.display.flip()
            dt = clock.tick(60) / 1000
            continue
        
        #
        screen.fill((0,0,16))
        pygame.display.flip()
        dt = clock.tick(60) / 1000
        
if __name__ == "__main__":
    main()

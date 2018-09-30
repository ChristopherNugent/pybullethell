import pygame
from game import Game

SIZE_X = 1000
SIZE_Y = 600
TICKS_PER_BULLET = 5

if __name__ == '__main__':
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption('pyBullethell')

    screen = pygame.display.set_mode((SIZE_X, SIZE_Y))
    clock = pygame.time.Clock()

    game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)
    game_exit = False
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        foreground = pygame.Surface((SIZE_X, SIZE_Y), pygame.SRCALPHA)
        foreground.fill(pygame.Color('black'))

        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            game = Game(SIZE_X, SIZE_Y, TICKS_PER_BULLET)

        game.tick()
        game.draw(foreground)

        screen.fill((60, 70, 90))
        screen.blit(foreground, (0, 0))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

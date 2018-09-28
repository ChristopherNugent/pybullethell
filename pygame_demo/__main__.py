import pygame
import random
import time
from objects import Player, Timer
import utils


if __name__ == '__main__':
    pygame.font.init()
    pygame.init()
    pygame.display.set_caption('PyGame demo')

    width, height = 540, 540
    screen = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    field = pygame.Rect(0, 0, 500, 500)
    player = Player(250, 250)

    bullets = []
    game_exit = False
    timer = None
    font = pygame.font.Font(None, 80)
    score_font = pygame.font.Font(None, 30)
    game_start = time.time()
    score = 0
    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
        foreground = pygame.Surface((500, 500), pygame.SRCALPHA)
        foreground.fill(pygame.Color('black'))

        # Update player and draw
        player.tick()
        player.draw(foreground)

        # Update bullets and draw
        for bullet in bullets:
            bullet.tick()
            bullet.draw(foreground)

        utils.draw_score(foreground, score_font, score)

        # Get all the bullet hitboxes
        bullet_hitboxes = [b.hitbox() for b in bullets]

        # Keep only bullets on the field
        bullets = [bullets[i] for i
                   in field.collidelistall(bullet_hitboxes)]

        if player.alive:
            score += 1

        # Check if player is killed
        if player.alive and player.hitbox().collidelist(bullet_hitboxes) != -1:
            player.alive = False
            bullets = utils.death_explosion(player.x, player.y)
            timer = Timer(5)

        # Spawn a new bullet
        if player.alive and not random.randrange(10):
            bullets.append(utils.random_bullet())

        # Restart game/show timers
        if timer is not None:
            if timer.is_done():
                player = Player(250, 250)
                bullets = []
                timer = None
                score = 0
            else:
                utils.draw_time_left(foreground, timer, font)

        screen.fill((60, 70, 90))
        screen.blit(foreground, (20, 20))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

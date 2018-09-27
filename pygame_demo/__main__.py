import pygame
import random
from itertools import permutations
from objects import Player, Bullet, Timer


# Get a random Bullet object, coming in from the end of the field
def random_bullet():
    max_speed = 3
    speed_x, speed_y = 0, 0
    while speed_x == 0 and speed_y == 0:
        speed_x = random.randrange(-max_speed, max_speed)
        speed_y = random.randrange(-max_speed, max_speed)
    axis = random.choice('xy')
    position = random.randrange(500)
    if axis == 'x':
        position_y = 0 if speed_y > 0 else 500
        return Bullet(position, position_y, speed_x, speed_y)
    else:
        position_x = 0 if speed_x > 0 else 500
        return Bullet(position_x, position, speed_x, speed_y)


# Get a list of bullets for the death animation
def death_explosion(x, y):
    return list([Bullet(x, y, xs, ys) for xs, ys
                 in permutations(list(range(-10, 10)), 2)
                 if (xs, ys) != (0, 0)])


# Get a pygame.Font object with a random font
def get_font():
    font_name = random.choice(pygame.font.get_fonts())
    print(font_name)
    return pygame.font.SysFont(font_name, 80)


# Draw the time left before thee next game starts
def draw_time_left(surface, timer, font):
    rendered_text = font.render('{:.2f}'.format(timer.time_left()), True,
                                pygame.Color('white'))
    surface.blit(rendered_text, (200, 200))


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
    font = None
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

        # Get all the bullet hitboxes
        bullet_hitboxes = [b.hitbox() for b in bullets]

        # Keep only bullets on the field
        bullets = [bullets[i] for i
                   in field.collidelistall(bullet_hitboxes)]

        # Check if player is killed
        if player.alive and player.hitbox().collidelist(bullet_hitboxes) != -1:
            player.alive = False
            bullets = death_explosion(player.x, player.y)
            timer = Timer(5)
            font = get_font()

        # Spawn a new bullet
        if player.alive and not random.randrange(30):
            bullets.append(random_bullet())

        # Restart game/show timers
        if timer is not None:
            if timer.is_done():
                player = Player(250, 250)
                bullets = []
                timer = None
            else:
                draw_time_left(foreground, timer, font)

        screen.fill((60, 70, 90))
        screen.blit(foreground, (20, 20))
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()

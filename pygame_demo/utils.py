import pygame
import random
from objects import Bullet
from itertools import permutations


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
def get_random_font():
    font_name = random.choice(pygame.font.get_fonts())
    print(font_name)
    return pygame.font.SysFont(font_name, 80)


# Draw the time left before thee next game starts
def draw_time_left(surface, timer, font):
    rendered_text = font.render('{:.2f}'.format(timer.time_left()), True,
                                pygame.Color('white'))
    surface.blit(rendered_text, (200, 200))


def draw_score(surface, font, score):
    rendered_text = font.render('{}'.format(score), True,
                                pygame.Color('white'))
    surface.blit(rendered_text, (10, 10))

from abc import ABC, abstractmethod
import pygame
import time


class GameObject(ABC):

    @abstractmethod
    def draw(self, surface):
        pass

    @abstractmethod
    def hitbox(self):
        pass

    @abstractmethod
    def tick(self):
        pass


class Player(GameObject):
    SPEED = 5
    SIZE = 30

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Player.SIZE, Player.SIZE)

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.x = max(0, min(self.x - Player.SPEED, 500 - Player.SIZE))
        if keys[pygame.K_RIGHT]:
            self.x = max(0, min(self.x + Player.SPEED, 500 - Player.SIZE))
        if keys[pygame.K_UP]:
            self.y = max(0, min(self.y - Player.SPEED, 500 - Player.SIZE))
        if keys[pygame.K_DOWN]:
            self.y = max(0, min(self.y + Player.SPEED, 500 - Player.SIZE))

    def draw(self, surface):
        if self.alive:
            color = (pygame.Color('blue') if self.alive
                     else pygame.Color('black'))
            pygame.draw.rect(surface, color,
                             (self.x, self.y, Player.SIZE, Player.SIZE))


class Bullet(GameObject):
    SIZE = 10

    def __init__(self, x, y, x_speed, y_speed):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Bullet.SIZE, Bullet.SIZE)

    def tick(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def draw(self, surface):
        pygame.draw.rect(surface, pygame.Color('red'),
                         (self.x, self.y, Bullet.SIZE, Bullet.SIZE))


class Timer:

    def __init__(self, time_s):
        self.finished = time.time() + time_s

    def is_done(self):
        return time.time() > self.finished

    def time_left(self):
        return self.finished - time.time()

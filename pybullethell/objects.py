from abc import ABC, abstractmethod
import pygame


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

    def __init__(self, x, y, game_size_x, game_size_y):
        self.x = x
        self.y = y
        self.game_size_x = game_size_x
        self.game_size_y = game_size_y
        self.alive = True

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Player.SIZE, Player.SIZE)

    def tick(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.x = max(0, min(self.x - Player.SPEED,
                                self.game_size_x - Player.SIZE))
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.x = max(0, min(self.x + Player.SPEED,
                                self.game_size_x - Player.SIZE))
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.y = max(0, min(self.y - Player.SPEED,
                                self.game_size_y - Player.SIZE))
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.y = max(0, min(self.y + Player.SPEED,
                                self.game_size_y - Player.SIZE))

    def draw(self, surface):
        if self.alive:
            color = (pygame.Color('white') if self.alive
                     else pygame.Color('black'))
            pygame.draw.rect(surface, color,
                             (self.x, self.y, Player.SIZE, Player.SIZE))


class Bullet(GameObject):
    SIZE = 10

    def __init__(self, x, y, x_speed, y_speed, color=pygame.Color('red')):
        self.x = x
        self.y = y
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.color = color

    def hitbox(self):
        return pygame.Rect(self.x, self.y, Bullet.SIZE, Bullet.SIZE)

    def tick(self):
        self.x = self.x + self.x_speed
        self.y = self.y + self.y_speed

    def draw(self, surface):
        pygame.draw.rect(surface, self.color,
                         (self.x, self.y, Bullet.SIZE, Bullet.SIZE))

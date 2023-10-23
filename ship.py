import pygame
import constants as c
from bullet import Bullet


class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('i size 2.png'))
        self.sprites.append(pygame.image.load('i size 2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = c.DISPLAY_WIDTH // 2
        self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.hp = 1
        self.lives = 1
        self.vel_x = 0
        self.vel_y = 0
        self.speed = 7.5

    def update(self):
        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]



        self.rect.x += self.vel_x
        if self.rect.x <= 0:
            self.rect.x = 0
        elif self.rect.x >= c.DISPLAY_WIDTH - self.rect.width:
            self.rect.x = c.DISPLAY_WIDTH - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= c.DISPLAY_HEIGHT - self.rect.height:
            self.rect.y = c.DISPLAY_HEIGHT - self.rect.height
        self.rect.y += self.vel_y

    def get_hit(self):
        self.hp -= 1
        if self.hp <= 0:
            self.hp = 0
            self.death()
        print(self.hp)

    def death(self):
        self.lives -= 1
        print(self.lives)
        if self.lives <= 0:
            self.lives = 0
        self.hp = 1
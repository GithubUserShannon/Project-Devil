import pygame
import constants as c
import random


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('speed devil1.png'))
        self.sprites.append(pygame.image.load('speed devil2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, c.DISPLAY_WIDTH - self.rect.width)
        self.rect.y = 700
        self.hp = 0
        self.score_value = 1
        self.vel_x = 0
        self.vel_y = -25
        self.speed = 500

    def update(self):
        print('t')
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.current_sprite += 1

        if self.current_sprite >= len(self.sprites):
            self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]

    def get_hit(self):
        self.hp -= 1
        if self.hp < 0:
            self.destroy()


    def destroy(self):
        self.kill()

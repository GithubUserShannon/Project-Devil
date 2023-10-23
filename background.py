import pygame
import constants as c
from star import Star
import random
from ship import Ship

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(c.DISPLAY_SIZE)
        self.color = (125, 125, 125)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1, 10)


    def update(self):
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= c.DISPLAY_HEIGHT:
                self.stars.remove(star)
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1
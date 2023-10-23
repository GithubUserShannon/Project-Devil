import pygame
import constants as c
import Score

class Design(pygame.sprite.Sprite):
    def __init__(self):
        super(Design, self).__init__()
        self.image = pygame.image.load('enemy.png').convert_alpha()
        self.rect = self.image.get_rect
        self.hp = 50
        self.score_value = 50
        self.vel_x = (2 - c.DISPLAY_HEIGHT) - 2
        self.vel_y = 0

    def spawn(self):
        if self.score_value == 15:
            def update():
                print('')

    def update(self):
        print('e')

    def get_hit(self):
        self.hp -= 1
        if self.hp < 0:
            self.destroy()

    def destroy(self):
        self.kill()

import pygame
from enemy import Enemy
import random


class EnemySpawner:
    def __init__(self):
        self.enemy_group = pygame.sprite.Group()
        self.spawn_timer = random.randrange(30, 120)

    def update(self):
        self.enemy_group.update()
        if self.spawn_timer == 0:
            self.spawn_enemy()
            self.spawn_timer = random.randrange(30, 120)
        else:
            self.spawn_timer -= 1

    def spawn_enemy(self):
        new_enemy = Enemy()
        self.enemy_group.add(new_enemy)



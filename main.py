import pygame
import random


DISPLAY_WIDTH = 1300
DISPLAY_HEIGHT = 700
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_HEIGHT)


#Functions
class Particle(pygame.sprite.Sprite):
    def __init__(self):
        super(Particle, self).__init__()
        self.width = random.randrange(1, 6)
        self.height = self.width
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255), random.randrange(1, 200))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.kill_timer = 60
        self.vel_x = random.randrange(-16, 16)
        self.vel_y = random.randrange(-16, 16)

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('speed devil1.png'))
        self.sprites.append(pygame.image.load('speed devil2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, DISPLAY_WIDTH - self.rect.width)
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

class ParticleSpawner:
    def __init__(self):
        self.particle_group = pygame.sprite.Group()

    def update(self):
        self.particle_group.update()


    def spawn_particles(self, pos):
        random_number = random.randrange(3, 30)
        for num_particles in range(random_number):
            new_particle = Particle()
            new_particle.rect.x = pos[0]
            new_particle.rect.y = pos[1]
            self.particle_group.add(new_particle)

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

class Ship(pygame.sprite.Sprite):
    def __init__(self):
        super(Ship, self).__init__()
        self.sprites = []
        self.sprites.append(pygame.image.load('i size 2.png'))
        self.sprites.append(pygame.image.load('i size 2.png'))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = DISPLAY_WIDTH // 2
        self.rect.y = DISPLAY_HEIGHT - self.rect.height
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
        elif self.rect.x >= DISPLAY_WIDTH - self.rect.width:
            self.rect.x = DISPLAY_WIDTH - self.rect.width
        if self.rect.y <= 0:
            self.rect.y = 0
        elif self.rect.y >= DISPLAY_HEIGHT - self.rect.height:
            self.rect.y = DISPLAY_HEIGHT - self.rect.height
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

class BG(pygame.sprite.Sprite):
    def __init__(self):
        super(BG, self).__init__()
        self.image = pygame.Surface(DISPLAY_SIZE)
        self.color = (255, 255, 255)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.stars = pygame.sprite.Group()
        self.timer = random.randrange(1, 10)


    def update(self):
        self.stars.update()
        for star in self.stars:
            if star.rect.y >= DISPLAY_HEIGHT:
                self.stars.remove(star)
        if self.timer == 0:
            new_star = Star()
            self.stars.add(new_star)
            self.timer = random.randrange(1, 10)
        self.image.fill(self.color)
        self.stars.draw(self.image)
        self.timer -= 1

class Star(pygame.sprite.Sprite):
    def __init__(self):
        super(Star, self).__init__()
        self.width = random.randrange(1, 3, 5)
        self.height = self.width + 100
        self.size = (self.width, self.height)
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 10), random.randrange(0, 20), random.randrange(0, 40), random.randrange(0, 30))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, DISPLAY_WIDTH)
        self.vel_x = 0
        self.vel_y = 70

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

pygame.display.set_caption('Sonic_Devil')
icon = pygame.image.load('Sonic Devils.png')
pygame.display.set_icon(icon)

pygame.init()
pygame.mixer.init()

display = pygame.display.set_mode(DISPLAY_SIZE)
fps = 60
clock = pygame.time.Clock()
black = (0, 0, 0)

#Place Function
bg = BG()
bg_group = pygame.sprite.Group()
bg_group.add(bg)
player = Ship()
sprite_group = pygame.sprite.Group()
sprite_group.add(player)
enemy_spawner = EnemySpawner()
particle_spawner = ParticleSpawner()
moving_sprites = pygame.sprite.Group()

pygame.mixer.music.load('Devil Chase.mp3')
pygame.mixer.music.set_volume(50)
pygame.mixer.music.play(loops=True)

#if clock is active movements and onscreen movement updates at 60 fps
running = True
while running:
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.vel_x = -player.speed
            elif event.key == pygame.K_d:
                player.vel_x = player.speed
            if event.key == pygame.K_w:
                player.vel_y = -player.speed
            elif event.key == pygame.K_s:
                player.vel_y = player.speed
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player.vel_x = 0
            elif event.key == pygame.k_w and pygame.K_d:
                player.vel_x = 0
            elif event.key == pygame.K_w and pygame.k_a:
                player.vel_y = 0.25
            if event.key == pygame.K_s:
                player.vel_y = -0.2

    particle_spawner.update()
    bg_group.update()
    sprite_group.update()
    enemy_spawner.update()
    moving_sprites.update(0.1)

    collided = pygame.sprite.groupcollide(sprite_group, enemy_spawner.enemy_group, False, False)
    for player, enemy in collided.items():
        enemy[0].hp = 0
        enemy[0].get_hit()
        player.get_hit()


    display.fill(black)
    bg_group.draw(display)
    sprite_group.draw(display)
    moving_sprites.draw(display)
    enemy_spawner.enemy_group.draw(display)
    particle_spawner.particle_group.draw(display)
    pygame.display.update()
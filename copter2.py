#!/usr/bin/python3
import pygame
import os

pygame.init()
width = 800
height = int(width*0.8)
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption('helicopter')

clock = pygame.time.Clock()
fps = 60

lef = False
rig = False
up = False
down = False
shoot = False

bg = (100, 100, 255)

#image1 = pygame.image.load('img\background\mountain.png')

awan = (0, 0, 0)

bullet_img = pygame.image.load('img/icons/bullet.png').convert_alpha()

def draw_bg():
    screen.fill(bg)
    pygame.draw.line(screen, awan,(0,610), (width, 610))
#   screen.blit(image1)
class data(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed, ammo):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.alive = True
        self.speed = speed
        self.health = 100
        self.flip = False
        self.ammo = ammo
        self.start_ammo = ammo
        # self.health = health
        self.max_health = self.health
        self.shoot_cooldown = 0
        self.direction = 1
        self.animation_list = []
        self.frame_index = 0
        self.action = 0
        self.update_time = pygame.time.get_ticks()

        animation_types = ['Idle', 'Move']
        for animation in animation_types:

            temp_list = []

            num_of_frames = len(os.listdir(f'img/{self.char_type}/{animation}'))
            for i in range(num_of_frames):
                img = pygame.image.load(f'img/{self.char_type}/{animation}/{i}.png').convert_alpha()
                img = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                temp_list.append(img)
            self.animation_list.append(temp_list)

        self.image = self.animation_list[self.action][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.update_animation()
        self.check_alive()
        if self.shoot_cooldown>0:
            self.shoot_cooldown -= 1

    def move(self, lef, rig):
        dx = 0
        dy = 0
        if lef:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if rig:
            dx = self.speed
            self.flip = False
            self.direction = 1

        self.rect.x += dx
        self.rect.y += dy
    def fly(self, up, down):
        dx = 0
        dy = 0
        if up:
            dy = -self.speed
            self.direction = -1
        if down:
            dy = self.speed
            self.direction = 1
        self.rect.x += dx
        self.rect.y += dy
   
    def shoot(self):
        if self.shoot_cooldown == 0 and self.ammo>0:
            self.shoot_cooldown = 20
            bullet = Bullet(self.rect.centerx + (1*self.rect.size[0]*self.direction), self.rect.centery, self.direction)
            bullet_group.add(bullet)
            self.ammo -= 1

    def update_animation(self):
        animation_cooldown = 100
        self.image = self.animation_list[self.action][self.frame_index]
        if pygame.time.get_ticks()-self.update_time > animation_cooldown:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list[self.action]):
            if self.action == 10:
                self.frame_index = len(self.animation_list[self.action])-1
            else:
                self.frame_index = 0
            
    def update_action(self, new_action):
        if new_action != self.action:
            self.action = new_action
            self.frame_index = 0
            self.update_time = pygame.time.get_ticks()

    def check_alive(self):
        if self.health <= 0:
            self.health = 0
            self.speed = 0
            self.alive = False
            self.update_action(3)

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, direction):
        pygame.sprite.Sprite.__init__(self)
        self.speed = 2
        self.image = bullet_img
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.direction = direction

    def update(self):
        self.rect.y += (self.direction * self.speed)

        if self.rect.right < 5 or self.rect.left > width:
            self.kill()

        if pygame.sprite.spritecollide(player, bullet_group, False):
            if player.alive:
                player.health -= 5
                self.kill()
                        
        # if pygame.sprite.spritecollide(enemy, bullet_group, False):
        #     if enemy.alive:
        #         enemy.health -= 25
        #         self.kill()


bullet_group = pygame.sprite.Group()

player = data('player', 200, 320, 1, 1, 1000)

run = True
while run:

    clock.tick(fps)

    draw_bg()
    player.update()
    player.draw()

    bullet_group.update()
    bullet_group.draw(screen)

    if player.alive:
        if shoot:
            player.shoot()
        if lef or rig:
            player.update_action(1)
        else:
            player.update_action(0)
        player.move(lef, rig)   
        player.fly(up, down)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lef = True
            if event.key == pygame.K_RIGHT:
                rig = True
            if event.key == pygame.K_UP:
                up = True
            if event.key == pygame.K_DOWN:
                down = True
            if event.key == pygame.K_SPACE:
                shoot = True
            #if event.key == pygame.K_a:
                         #       lef = True
                        #if event.key == pygame.K_d:
                         #       rig = True
                        #if event.key == pygame.K_w:
                         #       up = True
                        #if event.key == pygame.K_s:
                          #      down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                lef = False
            if event.key == pygame.K_RIGHT:
                rig = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN:
                down = False
            if event.key == pygame.K_SPACE:
                shoot = False
            #if event.key == pygame.K_a:
                        #        lef = False
                        #if event.key == pygame.K_d:
                         #       rig = False
                        #if event.key == pygame.K_w:
                          #      up = False
                        #if event.key == pygame.K_s:
                         #       down = False
    pygame.display.update()
pygame.quit()

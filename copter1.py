#!/usr/bin/python3
import pygame

pygame.init()

width, height = 800, 640


left = False
right = False

screen = pygame.display.set_mode((width, height))

background = (255,255,255)

def draw_background(): 
	screen.fill(background)

class data(pygame.sprite.Sprite):
	def __init__(self, char_type, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.char_type = char_type
		self.speed = speed
		self.flip = False
		self.direction = 1
		img = pygame.image.load(f'img/{self.char_type}/Idle/0.png')
		self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x, y)

	def move(self, left, right):
		dx = 0 
		dy = 0

		if left:
			dx = -self.speed
			self.flip = True
			# self.direction = -1
		if right:
			dx = self.speed
			self.flip = False
			# self.direction = 1

		self.rect.x += dx
		self.rect.y += dy
		

	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)#(flip(gmbar, diflip xFalse, y))
		
player = data('player', 200, 200, 2, 2)
run = True 

while run:
	screen.fill(background)
	
	player.draw()
	player.move(left, right)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				left = True
			if event.key == pygame.K_RIGHT:
				right = True
			# if event.key == pygame.K_UP:
			# 	up = True
			# if event.key == pygame.K_DOWN:
			# 	down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				left = False
			if event.key == pygame.K_RIGHT:
				right = False
			# if event.key == pygame.K_UP:
			# 	up = False
			# if event.key == pygame.K_DOWN:
			# 	down = False
		
	pygame.display.update() 

pygame.quit()
import pygame

pygame.init()

width, height = 800, 640

screen = pygame.display.set_mode((width, height))

m_left = False
m_right = False
m_up =False
m_down = False

bg = (100, 100, 255)

def gambar_bg():
	screen.fill(bg)

class data(pygame.sprite.Sprite):
	def __init__(self, gambar, x, y, scale, speed):
		pygame.sprite.Sprite.__init__(self)
		self.gambar = gambar 
		self.speed = speed
		self.direction = 1
		self.flip = False
		img = pygame.image.load(f'img/{self.gambar}/Idle/0.png')
		self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
		self.rect = self.image.get_rect()
		self.rect.center = (x,y)

	def move(self, m_left, m_right, m_up, m_down):
		dx = 0
		dy = 0

		if m_left:
			dx = -self.speed
			self.flip = True
			self.direction = -1

		if m_right:
			dx = self.speed
			self.flip = False
			self.direction = 1

		if m_up:
			dy = self.speed
			self.direction = 1

		if m_down:
			dy = -self.speed
			self.direction = -1

		self.rect.x +=dx
		self.rect.y +=dy

	def draw(self):
		screen.blit(pygame.transform.flip(self.image, self.flip, False),self.rect)

player = data('player', 200, 200, 1, 3)


run = True



while run:

	gambar_bg()
	player.draw()
	player.move(m_left, m_right, m_down, m_up)

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				m_left = True
			if event.key == pygame.K_RIGHT:
				m_right = True
			if event.key == pygame.K_UP:
				m_up = True
			if event.key == pygame.K_DOWN:
				m_down = True

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				m_left = False
			if event.key == pygame.K_RIGHT:
				m_right = False
			if event.key == pygame.K_UP:
				m_up = False
			if event.key == pygame.K_DOWN:
				m_down = False

	pygame.display.update()

pygame.quit()
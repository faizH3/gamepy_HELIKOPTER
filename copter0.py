import pygame

pygame.init()

width, height = 800, 640


screen = pygame.display.set_mode((width, height))

background = (255,255,255)

def draw_bg(): #function
	screen.fill(background)

run = True #data type boolean

while run:
	#call function draw_bg() and than you can look this in console
	draw_bg()

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			run = False

		if event.type == pygame.KEYDOWN:
			if event. key == pygame.K_1:
				exit()

	pygame.display.update() #kita update layar

pygame.quit() #kondisi untuk keluar saat ditekan tombol exit
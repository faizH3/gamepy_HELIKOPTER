# pertama import module pygame
import pygame

pygame.init()

# tentukan lebar,tinggi layar
width, height = 800, 640

# buat variabel untuk men setting layar
screen = pygame.display.set_mode((width, height))

<<<<<<< HEAD
background = (255,255,255)
=======

background = (255,255,255)#RGB
>>>>>>> cbea9acaefe87ba401a28e1d7877d452386c4861

# ada beberapa cara penulisan melooping background
# 1 dengan membuat fungsi
# 2 langsung menempatkan code warna didalam looping
def draw_bg(): #function
	screen.fill(background)

run = True #data type boolean

while run:
	#call function draw_bg() and than you can look this in console
	
	draw_bg()

	for event in pygame.event.get():
		
		if event.type == pygame.QUIT:
			run = False

<<<<<<< HEAD
		if event.type == pygame.KEYDOWN:
			if event. key == pygame.K_1:
=======
		if event.type == pygame.KEYDOWN: # on press keyboards
			if event.key == pygame.K_1:
>>>>>>> cbea9acaefe87ba401a28e1d7877d452386c4861
				exit()

	pygame.display.update() #kita update layar

pygame.quit() #kondisi untuk keluar saat ditekan tombol exit
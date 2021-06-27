import pygame

pygame.init()

lebar = 800
tinggi = int(lebar*0.8)

layar = pygame.display.set_mode((lebar, tinggi))

gerak_kiri = False
gerak_kanan = False

terbang = False
turun = False

bg = (255, 255, 0)

class data(pygame.sprite.Sprite):
	def __init__(self, pengganti_folder, x, y, skala_gambar, kecepatan):
		pygame.sprite.Sprite.__init__(self)
		self.pengganti_folder = pengganti_folder
		self.kecepatan = kecepatan
		self.balik_gambar = False
		self.posisi = 1
		gmbr = pygame.image.load(f'img/{self.pengganti_folder}/Idle/0.png')
		self.gambar = pygame.transform.scale(gmbr, (int(gmbr.get_width()*skala_gambar), int(gmbr.get_height()*skala_gambar)))
		self.kotak_gambar = self.gambar.get_rect()
		self.kotak_gambar.center = (x, y)

	def gerak(self, gerak_kiri, gerak_kanan):
		dx = 0
		dy = 0

		if gerak_kiri:
			dx = -self.kecepatan
			self.balik_gambar = True
		# self.kotak_gambar.x += dx==-self.kecepatan

		if gerak_kanan:
			dx = self.kecepatan
			self.balik_gambar = False
		# self.kotak_gambar.x ++dx==self.kecepatan
		self.kotak_gambar.x += dx
		self.kotak_gambar.y += dy
	def gambarkan(self):
		layar.blit(pygame.transform.flip(self.gambar, self.balik_gambar, False), self.kotak_gambar)

pemain = data('player', 200, 200, 2, 2)

jalankan = True

while jalankan:

	layar.fill(bg)
	pemain.gambarkan()
	pemain.gerak(gerak_kiri, gerak_kanan)
	for jalan in pygame.event.get():
		if jalan.type == pygame.QUIT:
			jalankan = False

		if jalan.type == pygame.KEYDOWN:
			if jalan.key == pygame.K_LEFT:
				gerak_kiri = True
			if jalan.key == pygame.K_RIGHT:
				gerak_kanan = True
			# if jalan.key == pygame.K_UP:
			# 	terbang = True
			# if jalan.key == pygame.K_DOWN:
			# 	turun = True

		if jalan.type == pygame.KEYUP:
			if jalan.key == pygame.K_LEFT:
				gerak_kiri = False
			if jalan.key == pygame.K_RIGHT:
				gerak_kanan = False
			# if jalan.key == pygame.K_UP:
			# 	terbang = False
			# if jalan.key == pygame.K_DOWN:
			# 	turun = False
	pygame.display.update()

pygame.quit()
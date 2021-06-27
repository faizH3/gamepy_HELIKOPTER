import pygame

pygame.init()

width = 800
height = int(width*0.8)

screen = pygame.display.set_mode((width, height))



pygame.display.set_caption('shooter')
pygame.display.set_icon(pygame.image.load('img/player/player.png'))


class tentara(pygame.sprite.Sprite):
        def __init__(self, x, y, scale):
                pygame.sprite.Sprite.__init__(self)
                img = pygame.image.load('img/player/player.png')
                background = pygame.image.load('img/background/mountain.png')                
                self.image = pygame.transform.scale(img, (int(img.get_width()*scale), int(img.get_height()*scale)))
                self.bg = pygame.transform.scale(background, (int(background.get_width()*scale), int(backgrund.get_height()*scale)))
                self.rect = self.image.get_rect()
                self.rect = self.bg.get_rect()
                self.rect.center = (x,y)
        def draw(self):
                
                screen.blit(self.image, self.rect)
                screen.blit(self.bg, self.rect)
                

blue = [0,0,255]

#screen.fill((255,255,255))

pygame.draw.rect(screen, blue, [0,600,800,320])


pygame.display.flip()
                
player = tentara(200, 200, 1)
player2 = tentara(400, 200, 1)

run = True

while run:
        player.draw()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:

                        run = False


        pygame.display.update()

pygame.quit()
                        

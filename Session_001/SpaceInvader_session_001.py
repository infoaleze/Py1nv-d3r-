import pygame

pygame.init()
fenetre = pygame.display.set_mode((750,750))
pygame.display.set_caption('Sp@c3 1nv@d3r5')


noir = ((0,0,0))
blanc = (255,255,255)
vert = (0 , 255, 0)
red = (255,0,0)


class Vaisseau(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,25])
        self.image.fill(vert)
        self.rect = self.image.get_rect()  #rectangle de colision
        self.vie = 5 # nombre de vie

    def draw(self):

        fenetre.blit(self.image, (self.rect.x, self.rect.y))



mon_vaisseau = Vaisseau()

mon_vaisseau.rect.x = 375
mon_vaisseau.rect.y = 650


def redessine():
    fenetre.fill(noir)

    mon_vaisseau.draw()

    pygame.display.update();



run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        mon_vaisseau.rect.x  += -10
    if key[pygame.K_RIGHT]:
        mon_vaisseau.rect.x  += 10


    redessine()

pygame.quit()
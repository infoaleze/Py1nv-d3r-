import pygame


noir = ((0,0,0))
blanc = (255,255,255)
vert = (0 , 255, 0)
red = (255,0,0)


# configuration de Base pour le moteur pyGame
pygame.init()
fenetre = pygame.display.set_mode((750,750))
pygame.display.set_caption('Sp@c3 1nv@d3r5')



# Sprite du Joueur

class Vaisseau(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([50,25])
        self.image.fill(vert)
        self.rect = self.image.get_rect()  #rectangle de colision
        self.live = 5 # nombre de vie

    def draw(self):

        fenetre.blit(self.image, (self.rect.x, self.rect.y))


# Sprite des Aliens

class Alien(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([25,25])
        self.image.fill(blanc)
        self.rect = self.image.get_rect()  #rectangle de colision


# Sprite des Bukers

class Bunker(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface([8,8])
        self.image.fill(vert)
        self.rect = self.image.get_rect()  #rectangle de colision


# Création des Sprite

mon_vaisseau = Vaisseau()
mon_vaisseau.rect.x = 375
mon_vaisseau.rect.y = 650


liste_aliens = pygame.sprite.Group();

# Création du tableau d'aliens
for ligne in range(1,6):
    for colonne in range (1,11):
        un_alien = Alien()
        un_alien.rect.x = 80 + (50 * colonne)
        un_alien.rect.y = 25 + (50 * ligne)
        liste_aliens.add(un_alien)


# Création du tableau des bunkers

liste_bunker = pygame.sprite.Group();

for n in range (3):
    for ligne in range (5):
        for colonne in range(10):
            un_bunker =  Bunker()
            un_bunker.rect.x = ( 50 + (275* n)) + (10 * colonne)
            un_bunker.rect.y = ( 500 + (10 * ligne))
            liste_bunker.add(un_bunker)






def redessine():
    fenetre.fill(noir)

    mon_vaisseau.draw()
    liste_aliens.draw(fenetre)
    liste_bunker.draw(fenetre)

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
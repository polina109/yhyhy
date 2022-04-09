from pygame import*
from random import*

game = True
clock = time.Clock()
o = display.set_mode((500, 500))

class gameobject(sprite.Sprite):
    def __init__ (self, x, y, shir, vis):
        self.image =  transform.scale(image.load(img), (70,70))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def ris(self):
        o.blit(self.image, (self.rect.x, self.rect.y)


player1 = gameobject('korova.webp')
player2 = gameobject('korova.webp')
sh = gameobject('bomba.png', 240, 250, 30,30)
dx = -1
dy = -1
speedx = 5
speedy = 5


while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    o.fill(228,255,0)
    sh.ris()
    player1.ris()
    player2.ris()
    sh.rect.x = sh.rect.x + speedx*dx
    sh.rect.y = sh.rect.y + speedy*dy
    if sh.rect.x <= 0:
        dx =* -1
        speedx = randint(3,5)
        speedy = randint(3,5)
    if sh.rect.x > 470:
        dx =* -1
        speedy = randint(3,5)
        speedx = randint(3,5)
    if sh.rect.y <= 0:
        dy =* -1
        speedy = randint(3,5)
        speedx = randint(3,5)
    if sh.rect.y > 470:
        dy =* -1
        speedy = randint(3,5)
        speedx = randint(3,5)

    display.update()
    clock.tick(40)













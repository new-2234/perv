#Создай собственный Шутер!

from pygame import *
from random import randint
from time import time as timer 
hirina = 700
vicota = 500
window = display.set_mode((700,500))
display.set_caption('Шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()
victrel = mixer.Sound('fire.ogg')
clock = time.Clock()
game = True
hiclovectrelov = 0
perezaradka = False
gizni = 3 
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, sizex, sizey, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (sizex, sizey))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed 
        if keys[K_RIGHT] and self.rect.x < hirina-80:
            self.rect.x += self.speed 
    def fire(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top, 15, 20, -15)
        bullets.add(bullet)

finih = False
lost = 0
igrok = Player('rocket.png' , 300, 300, 80, 100, 10)
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y>vicota:
            self.rect.x = randint(80, hirina-80)
            self.rect.y = 0 
            lost = lost + 1 
class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()
bullets = sprite.Group()


monsters = sprite.Group()
for i in range (1,6):
    monster = Enemy('ufo.png', randint(80, hirina - 80), -40, 80, 50, randint (1,5)   )
    monsters.add(monster)
asteroids = sprite.Group()
for i in range(1, 3):
    asteroid = Enemy('asteroid.png', randint(30, hirina -30), -40, 80, 50, randint (1, 7))
    asteroids.add(asteroid)


font.init()
font2 = font.SysFont(None, 36)
ohci = 0 
font1 = font.SysFont(None, 80 )
win = font1.render('Вы победили', True, (0, 255, 0))
loser = font1.render('Вы проиграли', True, (250, 0, 0))
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                if hiclovectrelov < 5 and perezaradka == False:
                    hiclovectrelov += 1
                    victrel.play()
                    igrok.fire()
                if hiclovectrelov >= 5 and perezaradka == False:
                    vrema2 = timer()
                    perezaradka = True


    if not finih:

        window.blit(background, (0, 0))
        text = font2.render('счет: ' + str(ohci), 1, (255, 255, 0) )
        window.blit(text, (10,20))
        proisrih = font2.render('пропущенно: ' + str(lost) , 1, (255, 255, 0) )
        window.blit(proisrih, (10, 50))
        igrok.update()
        bullets.update()
        bullets.draw(window)
        igrok.reset()
        monsters.update()
        asteroids.update()
        asteroids.draw(window)
        monsters.draw(window)
        if perezaradka == True:
            vrema1 = timer()
            if vrema1 - vrema2 < 3:
                textperezaradka  = font2.render('перезарядка, подождите', 1 , (200,  0 , 0))
                window.blit(textperezaradka, (260, 460))
            else:
                hiclovectrelov = 0 
                perezaradka = False


#TODO
        ctolknovenie = sprite.groupcollide(monsters, bullets, True, True)
        for i in ctolknovenie:
            ohci += 1
            monster = Enemy('ufo.png', randint(80, hirina - 80), -40, 80, 50, randint (1,5)   )
            monsters.add(monster)
            if sprite.spritecollide(igrok, monsters, False ) or sprite.spritecollide(igrok, asteroids, False ) :
                
        
                sprite.spritecollide(igrok, monsters, True)
                sprite.spritecollide(igrok, asteroids, True)
                gizni -= 1
        if gizni == 0 or lost >= 5:
            finih = True
            window.blit(loser, (200, 200))

        if ohci>=4:
            finih = True
            window.blit(win, (200, 200))
        if gizni == 3:
            color = (255, 0 , 255)
        if gizni == 2:
            color =(255, 255, 0)
        if gizni == 1:
            color= (200, 200, 200)
        textgizni = font1.render(str(gizni), 1, color)
        window.blit(textgizni, (650, 10))
        display. update()
    else:
        finih =False 
        ohci = 0
        lost = 0
        hiclovectrelov = 0
        gizni =3 
        for i in bullets:
            i.kill()
        for i in monsters:
            i.kill()
        time.delay(3000)
        for i in range (1,6):
            monster = Enemy('ufo.png', randint(80, hirina - 80), -40, 80, 50, randint (1,5)   )
            monsters.add(monster)

    time.delay(50)





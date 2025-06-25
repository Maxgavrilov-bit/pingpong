from pygame  import *

class GameSprite(sprite.Sprite):
    def __init__(self, image_name, speed, x, y, width, length):
        super().__init__()
        self.image = transform.scale(image.load(image_name) , (length, width))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def reset(self):
        window.blit(self.image , (self.rect.x , self.rect.y))


class Player(GameSprite):
    def __init__(self, image_name, speed, x, y, width, length):
        super().__init__( image_name, speed, x, y, width, length)
        self.count = 0
        self.hp = 3
    def updater(self):
        if keys_pressed[K_UP] and self.rect.y > 49:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 450:
            self.rect.y += self.speed
    def updatel(self):
        if keys_pressed[K_W] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_S] and self.rect.y < 600:
            self.rect.y += self.speed

clock = time.Clock()
FPS = 60
window = display.set_mode((700, 500))
display.set_caption('ping pong')
window.fill((5, 30, 200))
final = False
while final != True:
    clock.tick(FPS)
    display.update()
    
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
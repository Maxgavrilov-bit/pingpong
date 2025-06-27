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
        if keys_pressed[K_UP] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 400:
            self.rect.y += self.speed
    def updatel(self):
        if keys_pressed[K_w] and self.rect.y > 10:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 400:
            self.rect.y += self.speed


class Ball(GameSprite):
    def __init__(self, image_name, speed, x, y, width, length):
        super().__init__( image_name, speed, x, y, width, length)
    def update(self):
        pass

    
ball1 = Ball('ball.png' , 15, 350, 250, 50, 50)
platform1 = Player('i.webp' , 10, 40, 200, 100, 30)
platform2 = Player('i.webp' , 10, 640, 200, 100, 30)
clock = time.Clock()
FPS = 60
window = display.set_mode((700, 500))
display.set_caption('ping pong')
window.fill((10, 200, 242))
game = True
while game:
    clock.tick(FPS)
    display.update()
    window.fill((10, 200, 242))
    keys_pressed = key.get_pressed()
    for e in event.get():
        if e.type == QUIT:
            game = False
    platform1.reset()
    platform2.reset()
    platform1.updatel()
    platform2.updater()
    ball1.reset()

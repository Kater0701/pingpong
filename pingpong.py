from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пингпонг')
window.fill((200, 255, 255))
clock = time.Clock()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, sprite_x, sprite_y, speed, w, h, direction=None):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (w, h))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        self.direction = direction
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_right(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP]:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN]:
            self.rect.y += self.speed
    def update_left(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w]:
            self.rect.y -= self.speed
        if key_pressed[K_s]:
            self.rect.y += self.speed

game = True
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)
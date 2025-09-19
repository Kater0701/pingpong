from pygame import *

window = display.set_mode((700, 500))
display.set_caption('Пингпонг')
bg = (200, 255, 255)
window.fill(bg)
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

class Circle(GameSprite):
    def update(self):
        if self.direction[0] == 'right':
            self.rect.x += self.speed
        if self.direction[0] == 'left':
            self.rect.x -= self.speed
        if self.direction[1] == 'down':
            self.rect.y += self.speed
        if self.direction[1] == 'up':
            self.rect.y -= self.speed
Player_left = Player('rectangle.png', 10, 10, 3, 25, 75)
Player_right = Player('rectangle.png', 665, 10, 3, 25, 75)
Ball = Circle('ball_tennis.png', 325, 225, 2, 50, 50, ['left', 'down'])

game = True
while game:
    window.fill(bg)
    Ball.reset()
    Ball.update()
    Player_left.reset()
    Player_left.update_left()
    Player_right.reset()
    Player_right.update_right()

    for e in event.get():
        if e.type == QUIT:
            game = False
    display.update()
    clock.tick(60)

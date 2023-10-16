import pygame
group = pygame.sprite.Group()
class Player(object):
    def __init__(self):
        self.image = pygame.image.load('Radish.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.midbottom = (100, screen_height - 130)
        self.vel_y = 0
        self.jumped = False
    def update(self):
        x_move = 0
        y_move = 0
        # 获取按键，并进行相应的移动
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            self.vel_y = -18
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            x_move -= 6
        if key[pygame.K_RIGHT]:
            x_move += 6
        # 添加角色重力（跳跃之后自然下落）
        self.vel_y += 1.5
        if self.vel_y > 18:
            self.vel_y = 18
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move
        # 控制人物的最低位置
        if self.rect.bottom > screen_height - 107:
            self.rect.bottom = screen_height - 107
        screen.blit(self.image, self.rect)
class Cloud(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('Flappy bird.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def update(self):
        self.rect.x -= 5
        screen.blit(self.image, self.rect)
        if self.rect.x < -1480:
            self.rect.x = 1480
# --------------------------------加载基本的窗口和时钟----------------------------
pygame.init()
screen_width = 1400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Flappy Bird 0.0')
clock = pygame.time.Clock()  # 设置时钟
# -------------------------------- 加载对象 ----------------------------------
bg = pygame.image.load("Radish.jpg").convert()
player = Player()
cloud1 = Cloud(0, 0)
cloud2 = Cloud(1400, 0)
# -------------------------------- 游戏主循环 ----------------------------------
run = True
while run:
    clock.tick(60)
    screen.blit(bg, (0, 0))
    cloud1.update()
    cloud2.update()
    player.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
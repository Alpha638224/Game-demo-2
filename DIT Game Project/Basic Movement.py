import pygame
class Player(object):
    def __init__(radish):
        radish.image = pygame.image.load('Radish.jpg').convert_alpha()
        radish.rect = radish.image.get_rect()
        radish.rect.midbottom = (100, screen_height - 130)
        radish.vel_y = 0
        radish.jumped = False
    def update(radish):
        x_move = 0
        y_move = 0
        # 获取按键，并进行相应的移动
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and radish.jumped is False:
            radish.vel_y = -18
            radish.jumped = True
        if not key[pygame.K_SPACE]:
            radish.jumped = False
        if key[pygame.K_LEFT]:
            x_move -= 6
        if key[pygame.K_RIGHT]:
            x_move += 6
        # 添加角色重力（跳跃之后自然下落）
        radish.vel_y += 1.5
        if radish.vel_y > 18:
            radish.vel_y = 18
        y_move += radish.vel_y
        radish.rect.x += x_move
        radish.rect.y += y_move
        # 控制人物的最低位置
        if radish.rect.bottom > screen_height - 107:
            radish.rect.bottom = screen_height - 107
        screen.blit(radish.image, radish.rect)
class Cloud(object):
    def __init__(self, x, y):
        self.image = pygame.image.load('Background.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def update(self):
        screen.blit(self.image, self.rect)
# --------------------------------加载基本的窗口和时钟----------------------------
pygame.init()
screen_width = 1400
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))
screen.fill((255,255,255))  # 填充为白色屏幕
pygame.display.set_caption('Radish 0.0')
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
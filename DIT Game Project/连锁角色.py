import pygame
screen_width = 1400
screen_height = 700
class Player(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load(filename)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False
    def update(self,filename,location):
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
        self.image = pygame.image.load('Background.jpg').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
    def update(self):
        screen.blit(self.image, self.rect)
pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Genshin Impact')
screen.fill((255,255,255))  # 填充为白色屏幕
player1 = Player("Radish.jpg",(100,200))  # 碰撞检测，必须有两个精灵，因此再创建一个精灵，并使用location来设定第二个精灵的位置
player2 = Player("RhythmQuest.jpeg",(300,200))
crash_result = pygame.sprite.collide_rect(player1,player2)  # 调用collide_rect()进行矩形区域检测，返回一个布尔值，碰撞返回True，否则返回False
background = pygame.image.load("Radish.jpg").convert()
clock = pygame.time.Clock()
cloud1 = Cloud(0, 0)
cloud2 = Cloud(1400, 0)
while True:
    clock.tick(60)
    screen.blit(background, (0, 0))
    cloud1.update()
    cloud2.update()
    screen.blit(player1.image,player1.rect)  # 绘制精灵到屏幕上
    screen.blit(player2.image,player2.rect)
    player1.update("Radish.jpg",(100,100))
    player2.update("RhythmQuest.jpeg",(200,200))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    pygame.display.update()  # 刷新显示屏幕
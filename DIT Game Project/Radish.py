import pygame
import time

screen_width = 1400
screen_height = 750
a = 0
b = 2
c = 2
level = 0
jump_time = 0

class Player(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load(filename)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False
    def jump(self):
        self.vel_y = -17
        self.jumped = True
    def update(self,filename,location):
        x_move = 0
        y_move = 0
        # 获取按键，并进行相应的移动
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE] and self.jumped is False:
            self.vel_y = -17
            self.jumped = True
        if not key[pygame.K_SPACE]:
            self.jumped = False
        if key[pygame.K_LEFT]:
            x_move -= 5.5
        if key[pygame.K_RIGHT]:
            x_move += 5.5
        if key[pygame.K_UP]:
            player.rect.y -= 200
            time.sleep(0.5)
            player.jump()
        if key[pygame.K_DOWN]:
            player.rect.x += 250
            player.rect.y -= 17
            time.sleep(0.5)
            player.jump()
        if key[pygame.K_RETURN]:
            player.rect.x += 60
            player.rect.y -= 17
            time.sleep(0.045)
        if key[pygame.K_BACKSPACE]:
            player.rect.x -= 60
            player.rect.y -= 17
            time.sleep(0.045)
        if key[pygame.K_TAB] and self.jumped == False:
            self.vel_y = -12
            self.jumped = True
        # 添加角色重力（跳跃之后自然下落）
        self.vel_y += 1.5
        if self.vel_y > 17:
            self.vel_y = 17
        y_move += self.vel_y
        self.rect.x += x_move
        self.rect.y += y_move
        # 控制人物的最低位置
        if player.rect.y > 1600:
            player.rect.x = 100
            player.rect.y = 300
        if level == 0 or level == 1 or level == 2:
            if self.rect.bottom > screen_height - 157 and (self.rect.x < 528 or (self.rect.x > 688 and self.rect.x < 952) or self.rect.x > 1100):
                self.rect.bottom = screen_height - 157
            screen.blit(self.image, self.rect)
        if level == 3:
            if self.rect.bottom > screen_height - 157 and self.rect.x < 430:
                self.rect.bottom = screen_height - 157
            elif self.rect.bottom > screen_height - 250 and self.rect.x > 430 and self.rect.x < 699:
                self.rect.bottom = screen_height - 250
            elif self.rect.bottom > screen_height - 270 and self.rect.x > 700 and self.rect.x < 944:
                self.rect.bottom = screen_height - 270
            elif self.rect.bottom > screen_height - 157 and self.rect.x > 945:
                self.rect.bottom = screen_height - 157
            screen.blit(self.image, self.rect)
        if level == 4 or level == 5:
            if self.rect.bottom > screen_height - 157:
                self.rect.bottom = screen_height - 157
            screen.blit(self.image, self.rect)
        if level == 6:
            if self.rect.bottom > screen_height - 157 and self.rect.x < 230:
                self.rect.bottom = screen_height - 157
            if self.rect.bottom > screen_height - 257 and self.rect.x > 1088:
                self.rect.bottom = screen_height - 257
            screen.blit(self.image, self.rect)
        if level == 7:
            if self.rect.bottom > screen_height - 157 and self.rect.x < 499:
                self.rect.bottom = screen_height - 157
            if self.rect.bottom > screen_height - 510 and self.rect.x > 525 and self.rect.x < 665:
                self.rect.bottom = screen_height - 510
            if self.rect.bottom > screen_height - 550 and self.rect.x > 1082:
                self.rect.bottom = screen_height - 550
            screen.blit(self.image, self.rect)
            
class Enemy(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load("slime.png")  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False
            
class Balloon(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load("balloon.png")  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False
        
class Ladder(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load("ladder.png")  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.vel_y = 0
        self.jumped = False

class Ground(pygame.sprite.Sprite):
    def __init__(self,filename,location):  # 定义构造函数
        pygame.sprite.Sprite.__init__(self)  # 调父类来初始化子类
        self.image = pygame.image.load(filename)  # 加载图片
        self.rect = self.image.get_rect()  # 获取图片rect区域
        self.rect.topleft = location  # 设置位置
        self.jumped = False
    def update(self,filename,location):
        screen.blit(self.image, self.rect)

pygame.init()  # 初始化pygame
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Radish 0.0')  # 设置窗口名称
screen.fill((255,255,255))  # 填充为白色屏幕
player = Player("Radish.jpg",(100,300))
ground = Ground("Level3.png",(-290,593))
ground1 = Ground("Level3.png",(525,593))
ground2 = Ground("ground3.png",(756,593))
ground3 = Ground("ground3.png",(1165,593))
ground4 = Ground("platform.png",(1500,600))
ground5 = Ground("platform.png",(1500,600))
ground6 = Ground("platform.png",(1500,600))
ground7 = Ground("small_platform.png",(600,240))
ocean = Ground("ocean.png",(200,710))
flag = Ground("flag.png",(1185,302))
slime = Enemy("slime.png",(600,538))
balloon = Balloon("balloon.png",(375,480))
balloon2 = Balloon("balloon.png",(625,480))
balloon3 = Balloon("balloon.png",(875,480))
ladder = Ladder("ladder.png",(360,230))
space = pygame.image.load("space.png").convert()
level_completed = pygame.image.load("level_completed.png").convert()
finished = pygame.image.load("finished.png").convert()
game_over = pygame.image.load("game_over.png").convert()
clock = pygame.time.Clock()
level = 1

while True:
    screen.blit(space, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key = pygame.key.get_pressed()
    if key[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    flag.update("0.jpg",(0,0))
    screen.blit(player.image,player.rect)  # 绘制精灵到屏幕上
    screen.blit(ground.image,ground.rect)
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground3.update("0.jpg",(0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == key[pygame.K_SPACE]:
                jump_time += 1
                if jump_time < 2:
                    player.jump()
                if jump_time >= 2:
                    time.sleep(1)
                    
    if player.rect.x > 1160:
        break
    pygame.display.update()  # 刷新显示屏幕
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
player.rect.x = 100
player.rect.y = 520
ground.rect.x = -500
ground4.rect.x = 500
ground4.rect.y = 592
ground5.rect.x = 766
ground5.rect.y = 592
ground6.rect.x = 911
ground6.rect.y = 592
ground2.rect.x = 1175
level = 2
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    flag.update("0.jpg",(0,0))
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground4.update("0.jpg",(0,0))
    ground5.update("0.jpg",(0,0))
    ground6.update("0.jpg",(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.rect.x > 1160:
        break
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
player.rect.x = 100
player.rect.y = 520
ground4.rect.y = 500
ground5.rect.y = 480
ground6.rect.y = 480
level = 3

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    flag.update("0.jpg",(0,0))
    player.update("0.jpg",(0,0))
    ocean.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground4.update("0.jpg",(0,0))
    ground5.update("0.jpg",(0,0))
    ground6.update("0.jpg",(0,0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if player.rect.x > 1160:
        break
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
level = 4
player.rect.x = 100
ground3 = Ground("ground3.png",(700,593))
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    flag.update("0.jpg",(0,0))
    player.update("0.jpg",(0,0))
    ocean.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground2.update("0.jpg",(0,0))
    ground3.update("0.jpg",(0,0))
    ground3.rect.x = ground3.rect.x + b
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    if ground3.rect.x > 800:
        b = -2
    if ground3.rect.x < 500:
        b = 2
    if player.rect.x > 1160:
        break
    
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
level = 5
player.rect.x = 100
ground = Ground("Level3.png",(-290,593))

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    screen.blit(slime.image,slime.rect)
    player.update("0.jpg",(0,0))
    slime.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground1.update("0.jpg",(0,0))
    slime.rect.x = slime.rect.x + c
    pygame.display.update()
    crash_result = pygame.sprite.collide_rect(player,slime)
    if crash_result == True:
        screen.blit(game_over, (550, 240))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
    if slime.rect.x > 850:
        c = -2
    if slime.rect.x < 550:
        c = 2
    if player.rect.x > 1160:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
level = 6
player.rect.x = 100
ground.rect.x -= 320
ground1.rect.x = 1160
ground1.rect.y -= 100
ground2.rect.x = 800
ground2.rect.y = 300
        
while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    screen.blit(balloon.image,balloon.rect)
    screen.blit(balloon2.image,balloon2.rect)
    screen.blit(balloon3.image,balloon3.rect)
    player.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground1.update("0.jpg",(0,0))
    balloon.update("0.jpg",(0,0))
    balloon2.update("0.jpg",(0,0))
    balloon3.update("0.jpg",(0,0))
    crash_result2 = pygame.sprite.collide_rect(player,balloon)
    crash_result3 = pygame.sprite.collide_rect(player,balloon2)
    crash_result4 = pygame.sprite.collide_rect(player,balloon3)
    if crash_result2 == True:
        player.rect.y -= 150
        player.jump()
    if crash_result3 == True:
        player.rect.y -= 150
        player.jump()
    if crash_result4 == True:
        player.rect.y -= 150
        player.jump()
    pygame.display.update()
    if player.rect.x > 1200:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
level = 7
player.rect.x = 100
ground1.rect.y = 200
balloon.rect.x = 860
balloon.rect.y = 220

while True:
    clock.tick(60)
    screen.fill((255,255,255))
    screen.blit(player.image,player.rect)
    screen.blit(ladder.image,ladder.rect)
    screen.blit(balloon.image,balloon.rect)
    player.update("0.jpg",(0,0))
    ladder.update("0.jpg",(0,0))
    balloon.update("0.jpg",(0,0))
    ground.update("0.jpg",(0,0))
    ground1.update("0.jpg",(0,0))
    ground7.update("0.jpg",(0,0))
    crash_result5 = pygame.sprite.collide_rect(player,ladder)
    crash_result6 = pygame.sprite.collide_rect(player,balloon)
    if crash_result5 == True:
        player.rect.y -= 18.5
    if crash_result6 == True:
        player.rect.y -= 150
        player.jump()
    pygame.display.update()
    if player.rect.x > 1200:
        break
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
while True:
    screen.blit(level_completed, (422, 240))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    key2 = pygame.key.get_pressed()
    if key2[pygame.K_SPACE]:
        break
    else:
        a = a + 0.01
        
while True:
    screen.blit(finished, (180, 270))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    time.sleep(3)
    pygame.quit() 
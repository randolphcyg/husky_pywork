import pygame
from pygame.sprite import Sprite
class Ship(Sprite):
    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置其初始位置'''
        #继承精灵
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像，并获取其外接矩形
        #load返回贴图所在文件
        self.image = pygame.image.load('images/ship.bmp')
        #矩形属性rect为贴图的矩形对象
        #get_rect()是一个处理矩形图像的方法，返回值包含矩形的居中属性（ center centerx centery ）
        #get_rect须加上（），否则后续程序在运行时会出现无法引用centerx和bottom的错误
        self.rect = self.image.get_rect()
        #先将表示屏幕的矩形储存在属性screen—rect中
        self.screen_rect = screen.get_rect()
        '''将每艘新飞船放在屏幕底部中央'''
        #再将self.rect.centerx设置为表示屏幕的矩形属性centerx
        #再将self.rect.bottom设置为表示屏幕的矩形属性bottom
        #后面使用这个rect属性来放置飞船在屏幕底部中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        #在飞船属性center中储存小数点
        self.center = float(self.rect.centerx)
        #添加属性，设置一个飞船向右移动的标志
        self.moving_right = False
        #添加一个飞船向左移动的标志
        self.moving_left = False
    def blitme(self):
        #方法blit 位块传输 将指定的像素内容传输到指定位置
        self.screen.blit(self.image,self.rect)
    def update(self):
        #根据标志来向右移动飞船
        #更新飞船的center值而不是rect（rect已被浮点化储存到center中）
        '''添加条件，防止飞船移动到屏幕外'''
        #以屏幕矩形的右边界为界，当按键事件（标志正确）以及飞船外接矩形坐标小于右边界时可向右移动
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        #根据标志向左移动飞船
        #以屏幕矩形的左边界为准，即x轴坐标的0，当按键事件（标志正确）以及飞船外接矩形坐标大于0时可向左移动
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        '''此处使用两个if来应对左右方向按键，两个条件同时检测，当同时按下左右键时，飞船纹丝不动，
        这有利于精准控制，如使用if—elif格式的话，if优先，故右键优先，同时按两个键时无法同时抵消，则向右移动'''
        #根据center来更新rect
        self.rect.centerx = self.center

    def center_ship(self):
        #让飞船底部居中
        self.center = self.screen_rect.centerx

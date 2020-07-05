#创建一个关于外星人的模块
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):

    '''表示单个外星人的类'''
    def __init__(self,ai_settings,screen):
        #继承精灵类
        super().__init__()
        self.ai_settings = ai_settings
        self.screen = screen
        #返回外星人图像并矩形化
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()
        #每个外星人最初都在屏幕左上角附近
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        #储存外星人的准确位置
        self.x = float(self.rect.x)


    def blitme(self):
        '''在指定位置绘制外星人'''
        self.screen.blit(self.image,self.rect)

    def update(self):
        #外星人坐标为速度乘以方向值，当方向值为负时方向改变
        self.x += (self.ai_settings.alien_speed_factor *
                    self.ai_settings.fleet_direction)
        self.rect.x = self.x
        '''当方向值为1时，x 坐标增加，向右移动。方向值为-1时，x 坐标减少，向左移动'''
    def check_edges(self):
        #检查外星人是否碰到了边缘
        #矩形化屏幕
        screen_rect = self.screen.get_rect()
        #当外星人贴图右边缘大于或等于屏幕矩形右边缘，返回正确
        if self.rect.right >= screen_rect.right:
            return True
        #当外星人贴图左边缘小于或等于屏幕矩形左边缘（小于等于0），返回正确
        elif self.rect.left <= screen_rect.left:
            return True


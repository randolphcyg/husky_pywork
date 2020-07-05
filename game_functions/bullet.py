#创建子弹类
import pygame
from pygame.sprite import Sprite
class Bullet(Sprite):
    '''一个对飞船发射的子弹进行管理的类'''
    def __init__(self,ai_settings,screen,ship):
        #通过函数super（）来继承sprite
        super().__init__()
        self.screen = screen
        #在（0，0）处创建一个代表子弹的矩形，再设置正确的位置,参数为初识坐标，子弹的宽和高
        self.rect = pygame.Rect(0,0,ai_settings.bullet_width,ai_settings.bullet_height)
        #根据飞船位置来确定子弹位置
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #储存用小数表示的子弹位置
        '''由于子弹是直线向下移动，所以我们只考虑在y轴上坐标的变化，
        而x轴的坐标是固定的，这由发射子弹时飞船的x轴坐标决定，
        因为我们在前面定义了self.rect.centerx = ship.rect.centerx'''
        self.y = float(self.rect.y)
        #储存子弹颜色
        self.color = ai_settings.bullet_bg_color
        #储存速度
        self.speed_factor = ai_settings.bullet_speed_factor
    def update(self):
        #让子弹向上移动
        self.y -= self.speed_factor
        #更新子弹rect的位置
        self.rect.y = self.y
    def draw_bullet(self):
        #在屏幕上绘制子弹
        pygame.draw.rect(self.screen,self.color,self.rect)


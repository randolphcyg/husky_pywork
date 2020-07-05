import pygame.ftfont
from pygame.sprite import Group
from ship import Ship
#导入json用于写入最高分
import json
#创建计分板类
class Scoreboard():
    def __init__(self,screen,ai_settings,stats):
        #初始化得分涉及的属性
        self.screen = screen
        self.screen_rect = self.screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats
        #设置计分板的字体
        self.text_color = (30,30,30)
        #默认字体，48字号
        self.ftfont = pygame.ftfont.SysFont(None,48)
        #准备初始得分图像和最高分图像、等级、飞船剩余图像
        self.prep_images()

    def prep_images(self):
        # 整合初始化图像内容
        self.prep_score()
        self.prep_high_score()
        self.prep_level()
        self.prep_ships()

    def prep_score(self):
        '''将得分转换为渲染的图像'''
        # 　得分为得分为10的整数倍，并将逗号用作千分位分隔符
        rounded_score = int(round(self.stats.score, -1))
        score_str = "{:,}".format(rounded_score)
        self.image = self.ftfont.render(score_str,True,self.text_color,self.ai_settings.bg_color)
        #将得分放在屏幕右上角
        #将文字渲染成的图像矩形化，指定位置
        self.score_rect = self.image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def prep_high_score(self):
        '''将最高得分渲染为图像'''
        #打开json文件读取最高分来圆整规范以及渲染为图像，当出现 FileNotFoundError 异常时创建json文件，并写入初始化最高分
        # （这一步仅需执行一次，也可应对文件丢失情况）

        try:
            with open('high_score.json') as f_obj:
                high_score_json = json.load(f_obj)
        except FileNotFoundError:
            with open('high_score.json','w') as f_obj:
                json.dump(self.stats.high_score,f_obj)

        # 最高得分为10的整数倍，并将逗号用作千位分隔符
        high_score = int(round(high_score_json,-1))
        high_score_str = "{:,}".format(high_score)


        self.high_score_image = self.ftfont.render(high_score_str,True,self.text_color,self.ai_settings.bg_color)
        #矩形化图像，并指定位置为屏幕顶端中央
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = self.score_rect.top

    def prep_level(self):
        '''将等级转化为渲染的图像'''
        self.level_image = self.ftfont.render(str(self.stats.level),True,self.text_color,self.ai_settings.bg_color)
        #将等级放在得分下方
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.score_rect.right
        self.level_rect.top = self.score_rect.bottom + 10

    def prep_ships(self):
        '''显示还剩余多少飞船'''
        self.ships = Group()
        #循环剩下的飞船数，并根据数量生成位置
        for ship_numbers in range(self.stats.ships_left):
            ship = Ship(self.ai_settings,self.screen)
            ship.rect.x = 10 + ship_numbers * (2 * ship.rect.width)
            ship.rect.y = -30
            self.ships.add(ship)




    def show_score(self):
        #在屏幕上显示得分和最高分
        self.screen.blit(self.image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.level_image,self.level_rect)
        #绘制飞船
        self.ships.draw(self.screen)


#创建一个游戏设置的类
class Settings:
    def __init__(self):
        #储存游戏初始化数据
        #初始化游戏的静态设置
        self.screen_width = 1400
        self.screen_height = 750
        self.bg_color = (200,200,200)
        #设置飞船数量
        self.ship_limit = 3
        #创建关于子弹的属性
        self.bullet_width = 15
        self.bullet_height = 30
        self.bullet_bg_color = (60,0,0)
        #设置限制子弹数量
        self.bullets_allowed = 3
        #设置外星人下降值
        self.alien_drop_factor = 2
        #设置速度提升倍数
        self.speedup_scale = 1.1
        #设置外星人点数的提高速度
        self.score_scale = 1.5
        #初始化速度值
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        #初始化动态设置
        # 设置外星人移动速度
        self.alien_speed_factor = 0.5
        # 设置外星人群移动值，向右为1，向左为-1
        self.fleet_direction = 1
        #设置外星人分数
        self.alien_points = 50
        #设置子弹移动速度
        self.bullet_speed_factor = 5
        # 设置飞船移动速度
        self.ship_speed_factor = 3

    def increase_speed(self):
        #提升速度值
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor*= self.speedup_scale
        #提升分数
        self.alien_points = int(self.alien_points * self.score_scale)

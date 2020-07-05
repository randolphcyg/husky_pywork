#游戏主程序
#模块sys可用于退出游戏，因为模块game_functions中已经导入sys，主程序中不需要再导入
import pygame
from settings import Settings
from ship import Ship
#导入信息统计类
from game_stats import GameStats
from scoreboard import Scoreboard
#导入编组
from pygame.sprite import Group
#由于不在主程序创建外星人实例，此处不必导入
#导入game_functions，后面的事件管理部分从模块导入
import game_functions as gf
#导入按钮类
from button import Button
def run_game():
    #初始化游戏并创建一个屏幕
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    #设置屏幕对象
    pygame.display.set_caption("alien_invision")
    #创建按钮类 形参msg对应的实参为“play”
    play_button = Button(ai_settings,screen,"Play")
    #创建一个用于储存游戏信息统计的实例
    stats = GameStats(ai_settings)
    #创建记分牌实例
    sb = Scoreboard(screen,ai_settings,stats)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)
    #创建一个子弹编组
    bullets = Group()
    #创建一个外星人编组
    aliens = Group()
    # 使用gf模块中的函数绘制外星人群
    gf.create_fleet(ai_settings,screen,ship,aliens)
    #开始游戏主循环
    while True:
        #使用模块game_funcations中的方法
        #check_events检测按键和鼠标点击事件
        gf.check_events(ai_settings,ship,screen,bullets,stats,play_button,aliens,sb)
        #当标志正确时运行游戏：
        if stats.game_active :
            #方法update（）用于确定事件标志以及移动距离和方向
            ship.update()
            #使用更新后的gf的函数用于更新和删除子弹
            #检测外星人与子弹的碰撞，删除外星人与子弹  并创建外星人群
            gf.update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb )
            #由于外星人会被子弹击中，所以在绘制子弹之后绘制外星人
            gf.update_aliens(ai_settings,ship,aliens,stats,bullets,screen,sb)
        #方法update_screen用于更新绘制屏幕各元素
        gf.update_screen(ai_settings,ship,screen,aliens,bullets,stats,play_button,sb)
        
#运行游戏
run_game()

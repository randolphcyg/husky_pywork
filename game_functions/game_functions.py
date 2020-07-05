#将管理事件的代码部分转移到此模块中，以简化主程序逻辑
import sys
import pygame
#导入子弹类
from bullet import Bullet
from alien import Alien
#导入json用于记录最高分
import json
#导入sleep来实现游戏暂停
from time import sleep

def fire_bullet(ai_settings,screen,ship,bullets):
    # 创建一个子弹，并将其加入到编组中去
    # 设置条件，限制子弹数量
    #当符合条件时，按下空格发射子弹
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def check_keydown_events(event,ai_settings,screen,ship,bullets,stats,aliens,sb):
    #响应按键
    if event.key == pygame.K_RIGHT:
        print("右")
        # 当按键事件为按下右箭头时,向右移动标志为正确
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        print("左")
        # 当按键事件为按下左箭头时，向左移动标志为正确
        ship.moving_left = True
        #当按下的键为z时
    elif event.key == pygame.K_z:
        print("Z键发送子弹")
        #简化keydown，当按下空格时调用函数fire_bullets检查条件发射子弹
        fire_bullet(ai_settings,screen,ship,bullets)
        #设置快捷键q用于退出游戏
    elif event.key == pygame.K_q:
        sys.exit()
        #设置快捷键p用于重置游戏
    elif event.key == pygame.K_p:
        start_game(stats,aliens,bullets,ai_settings,screen,ship,sb)

def check_keyup_events(event,ship):
    #响应松开
    if event.key == pygame.K_RIGHT:
        print("右松开")
        # 当按键事件为松开按右箭头时，向右移动标志为错误
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        print("左松开")
        # 当按键事件为松开按左箭头时，向左移动标志为错误
        ship.moving_left = False


def check_events(ai_settinngs,ship,screen,bullets,stats,play_button,aliens,sb):
    '''响应按键和鼠标事件'''
    for event in pygame.event.get():
        '''当事件类型为QUIT时，退出游戏'''
        if event.type == pygame.QUIT:
            sys.exit()
        #检测鼠标事件
        elif event.type == pygame.MOUSEBUTTONDOWN:
            #将鼠标点击区域坐标储存到变量中
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settinngs,screen,ship,sb)
       #更新后的check_event直接使用前面定义的函数
        elif event.type == pygame.KEYDOWN:
            #调用时增加形参
            check_keydown_events(event,ai_settinngs,screen,ship,bullets,stats,aliens,sb)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,ship)
            '''在 KEYDOWN 和 KEYUP 中使用 if-elif 结构处理两种按键标志，因为每个事件只与一个键关联，
            当同时按下左右两键时，即视为两个事件来处理'''


def check_play_button(stats,play_button,mouse_x,mouse_y,aliens,bullets,ai_settings,screen,ship,sb):
    '''在玩家单击play按钮时开始新游戏'''
    #将按钮点击检测储存到变量中
    button_clicked = play_button.rect.collidepoint(mouse_x,mouse_y)
    #当按钮被点击且游戏非运行状态时，按钮点击生效
    if button_clicked:
        #调用重置游戏方法
        start_game(stats,aliens,bullets,ai_settings,screen,ship,sb)

def start_game(stats,aliens,bullets,ai_settings,screen,ship,sb):
    '''创建重置游戏的方法'''
    if not stats.game_active :
        # 隐藏光标
        # 向set_visible（）传递参数False来隐藏光标
        pygame.mouse.set_visible(False)
        #重置速度
        ai_settings.initialize_dynamic_settings()
        # 重置统计信息
        stats.reset_stats()
        # 游戏运行标志正确
        stats.game_active = True
        #重置记分牌中的图像
        sb.prep_images()
        # 清空子弹和外星人
        aliens.empty()
        bullets.empty()
        # 创建新外星人群
        create_fleet(ai_settings, screen, ship, aliens)
        # 飞船居中
        ship.center_ship()

def update_bullets(bullets,aliens,ai_settings,screen,ship,stats,sb):
    # 对编组中的每一个子弹调用update
    #更新子弹位置
    bullets.update()
    # 删除已消失的子弹
    # 在for循环中不应从列表或编组删除条目，所以使用方法copy（）遍历编组的副本，然后修改编组
    # 遍历副本的原因：由于编组内的子弹是动态变化的，遍历副本后根据副本元素来删除编组中对应的元素，做到精准删除
    # 注意：这里删除的是原编组里的子弹！
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)
    #调用检测外星人子弹碰撞函数
    check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship,stats,sb)

def check_bullet_alien_collisions(bullets,aliens,ai_settings,screen,ship,stats,sb):
    #检查是否有子弹击中了外星人
    #如果子弹击中外星人，则删除该子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets,aliens,True,True)
    #当发生碰撞时加分
    if collisions :
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
            #检测是否出现新的最高分
            check_high_score(stats,sb)

    #当外星人团灭时，调用提升等级函数做出相应变化
    if len(aliens) == 0:
        start_new_level(bullets,ai_settings,stats,sb,screen,ship,aliens)

def start_new_level(bullets,ai_settings,stats,sb,screen,ship,aliens):
    # 清空子弹
    bullets.empty()
    # 提升外星人群速度
    ai_settings.increase_speed()
    # 提升等级
    stats.level += 1
    sb.prep_level()
    # 创建外星人
    create_fleet(ai_settings, screen, ship, aliens)

def check_high_score(stats,sb):
    '''检测是否诞生了新的最高分'''
    #读取json中的最高分，将最高分储存在变量，将当前分数与最高分比较
    #当当前分数高于最高分时，将当前最高分储存到新变量，并将新变量写入json文件
    #调用更新最高分函数，显示新的最高分
    with open('high_score.json') as f_obj:
        high_score = json.load(f_obj)
    if stats.score > high_score :
        new_high_score = stats.score
        with open('high_score.json','w') as f_obj :
            json.dump(new_high_score,f_obj)
    sb.prep_high_score()

def get_number_aliens_x(ai_settings,alien_width):
    '''整理函数，增加条理性'''
    '''此函数返回每行可容下的外星人数量'''
    # 按照公式来计算行的有效屏幕空间，需要与边界保持间距，间距为一个外星人矩形的宽，故行有效屏幕空间为屏宽减去两个外星人宽
    # 求一行容纳外星人数量：两个外星人之间需要保留一个外星人宽的间距，即一个外星人需要的宽为两倍外星人矩形宽
    # 那么行容纳外星人数量 = 行有效屏幕空间/两倍外星人矩形宽
    available_space_x = ai_settings.screen_width - 2 * alien_width  # 行外星人可用屏幕容量
    number_aliens_x = int(available_space_x / (2 * alien_width))  # 行容纳外星人数量
    '''这里使用了int来求得整数数量的外星人，舍弃了小部分，防止出现不完整外星人，同时也出于生成的目的，
       函数range()需要一个整数值'''
    return number_aliens_x

def get_number_rows(ai_settings, ship_height, alien_height):
    """计算屏幕可容纳多少行外星人"""
    # 屏幕垂直可用空间为屏幕高度减去第一行外星人高度和飞船高度，以及减去两倍外星人高度作为最底下一行外星人与飞船的距离
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    # 可容纳行数为屏幕垂直可用空间除以二倍外星人高度（外星人行与行之间保持一个外星人高度的间距）
    #公式中注意计算时的括号问题
    number_rows = int(available_space_y / (2 * alien_height))
    # 返回可容纳行数
    return number_rows

def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    '''创建单个外星人并将其放在行中'''
    # 先创建单个外星人
    # 外星人间距为外星人宽度
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 外星人位置从左算起，空掉一个外星人矩形作为间隔，每个外星人占据两个外星人矩形大小，
    # x 轴排布位置由for循环的外星人次序决定，故 * number_aliens_x
    alien.x = alien_width + 2 * alien_width * alien_number
    # 储存外星人坐标
    alien.rect.x = alien.x
    # 外星人行的位置需空出一行作为与顶的边界，同时行与行之间空出一个外星人高度作为间距
    # y 轴排布位置由for循环的行数次序决定，故 * row_number
    alien.rect.y = 30 + alien.rect.height + 2 * alien.rect.height * row_number
    # 将外星人添加到编组
    aliens.add(alien)

def create_fleet(ai_settings, screen, ship,aliens):
    '''创建外星人群'''
    # 创建一个外星人，计算每行外星人容量
    alien = Alien(ai_settings, screen)
    # 调用前面计算每行容量的函数，储存在变量中
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height,alien.rect.height)
    # 创建外星人群
    #遍历可用行空间和行数量，创造出相应数量的一群外星人
    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number,row_number)


#增加了子弹和外星人形参
def update_screen(ai_settings,ship,screen,aliens,bullets,stats,play_button,sb):
    '''设置、飞船、屏幕为三个实参，在方法中使用'''
    #屏幕颜色填充为设置中设置的颜色
    screen.fill(ai_settings.bg_color)
    #在飞船和外星人后面重绘所有子弹
    #绘制外星人编组中的每一个
    aliens.draw(screen)
    '''遍历编组中的每一个子弹，并对每一个子弹调用draw_bullte'''
    # 这里使用了方法bullets.sprites  它返回子弹编组  注意sprites是复数
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    #显示得分
    sb.show_score()
    #在背景设置完毕后将飞船绘制到指定位置
    ship.blitme()
    #当游戏处于非活动状态，绘制按钮
    if not stats.game_active :
        play_button.draw_button()
    #让最近绘制的屏幕可见
    pygame.display.flip()

def check_fleet_edges(ai_settings,aliens):
    #遍历每一个外星人，当触碰边缘时调用改变方向函数
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings,aliens)
            '''由于之前这里忘记break退出循环，外星人群有时会直接下落导致游戏结束'''
            break

def change_fleet_direction(ai_settings,aliens):
    #遍历每一个外星人，调整每一个外星人的 y 坐标，即下降
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.alien_drop_factor
    #改变方向值
    ai_settings.fleet_direction *= -1

def check_alien_bottom(ai_settings,ship,aliens,stats,bullets,screen,sb):
    #检查外星人是否触底
    #注意！！！
    #get_rect()要记得加上括号，不然会出现如下错误：
    # AttributeError: 'builtin_function_or_method' object has no attribute 'bottom'
    screen_rect = screen.get_rect()
    #遍历外星人编组
    for alien in aliens.sprites():
        #当有外星人触底时，调用ship_hit函数更新外星人和飞船
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb)
            break

def update_aliens(ai_settings,ship,aliens,stats,bullets,screen,sb):
    '''检查外星人是否触碰边缘，做出调整'''
    check_fleet_edges(ai_settings,aliens)
    # 对每个外星人的位置更新
    aliens.update()
    #检查外星人与飞船的碰撞，当碰撞时发出信号（已删去）
    #在碰撞时调用ship_hit，做出相应变化
    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb)
    #调用函数检查是否有外星人触底
    check_alien_bottom(ai_settings,ship,aliens,stats,bullets,screen,sb)


def ship_hit(stats,aliens,bullets,ai_settings,screen,ship,sb):
    #检查飞船数量是否用完，若未用完，暂停后更新飞船和外星人；若用完，标志False，没有更新，游戏结束
    if stats.ships_left > 0 :
        #响应被外星人撞到的飞船
        #飞船数量相应减一
        stats.ships_left -= 1
        #更新飞船剩余
        sb.prep_ships()
        #清空外星人和子弹列表
        aliens.empty()
        bullets.empty()
        #创建一群新的外星人
        create_fleet(ai_settings,screen,ship,aliens)
        #让飞船底部居中
        ship.center_ship
        #暂停0.5秒
        sleep(0.5)
    elif stats.ships_left == 0:
        #当飞船数量用完，标志错误，不执行更新
        stats.game_active = False
        #在游戏处于非运行状态时，光标出现，可以点击按钮继续游戏
        pygame.mouse.set_visible(True)


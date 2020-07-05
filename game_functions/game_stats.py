#创建游戏统计类
class GameStats():
    #跟踪游戏的统计信息
    def __init__(self,ai_settings):
        #初始化统计信息
        self.ai_setting = ai_settings
        #设置结束游戏的标志
        #修改标志，让游戏一开始处于非活动状态
        self.game_active = False
        #设置最高分，最高分不会被重置，所以在init初始化
        self.high_score = 0
        #在初始化init中调用方法reset_stats
        #在创建实例时能妥善地设置统计信息
        #在后续也可以调用
        self.reset_stats()
    def reset_stats(self):
        #重置统计
        #初始化游戏运行期间可能变化的统计信息
        #储存飞船数量
        self.ships_left = self.ai_setting.ship_limit
        #初始化得分
        self.score = 0
        #初始化等级
        self.level = 1

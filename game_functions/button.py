#创建按钮类
#导入模块ftfont（font），它能将文本渲染到屏幕上
import pygame.ftfont
class Button():
    def __init__(self,ai_settings,screen,msg):
        #初始化
        self.screen = screen
        self.screen_rect = screen.get_rect()
        #设置按钮尺寸和颜色
        self.wdith,self.height = 200,50
        self.button_color = (0,50,0)
        #指定文本颜色
        self.text_color = (255,255,255)
        #None 指定了使用默认字体渲染文本，48为字号
        self.ftfont = pygame.ftfont.SysFont(None,48)
        #创建一个rect对象
        self.rect = pygame.Rect(0,0,self.wdith,self.height)
        #rect对象位置居中
        self.rect.center = self.screen_rect.center
        #调用按钮标签（只需创建一次）
        self.prep_msg(msg)

    def prep_msg(self,msg):
        #创建渲染文本方法
        '''将msg渲染为图像，并使其在按钮上居中'''
        #将文本渲染为图像，第一个实参为文本，第二个实参为布尔值（用于指定图像边缘是否开启反锯齿功能,此处的Ture为开启）
        #第三个实参为文本颜色，第四个实参为按钮颜色（即图像的背景色，当没有指定时为透明）
        self.msg_image = self.ftfont.render(msg,True,self.text_color,self.button_color)
        #矩形化文本图像
        self.msg_image_rect = self.msg_image.get_rect()
        #文本图像位置居中，即在按钮中居中（按钮矩形的中央位置）
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        #绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color,self.rect)
        self.screen.blit(self.msg_image,self.msg_image_rect)


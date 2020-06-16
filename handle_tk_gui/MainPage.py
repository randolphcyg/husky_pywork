'''
@Author: randolph
@Date: 2020-06-13 00:12:42
@LastEditors: randolph
@LastEditTime: 2020-06-16 16:09:42
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 学生信息管理系统菜单跳转实现
'''
import tkinter as tk

from view import AboutFrame, CountFrame, DelFrame, InputFrame, UpdateFrame


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        width, height = 770, 380
        self.root.geometry('770x360+350+150')
        self.root.minsize(770, 380)
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)      # 创建不同Frame
        self.delPage = DelFrame(self.root)
        self.updatePage = UpdateFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)

        self.inputPage.grid()                       # 默认显示录入页面
        # 创建字体 
        menubar = tk.Menu(self.root)     # 菜单
        user_menubar = tk.Menu(menubar, tearoff=0)     # 用户子菜单 去掉虚线
        user_menubar.add_command(label="注销", command=self.logoff)
        # user_menubar.add_separator()
        user_menubar.add_command(label="退出", command=self.root.quit)
        menubar.add_cascade(label="用户选项", menu=user_menubar)
        # menubar.add_separator()
        menubar.add_command(label='录入', command=self.inputData)
        # menubar.add_separator()
        menubar.add_command(label='刪除', command=self.delData)
        # menubar.add_separator()
        menubar.add_command(label='修改', command=self.updateData)
        # menubar.add_separator()
        menubar.add_command(label='报表', command=self.countData)
        # menubar.add_separator()
        # 帮助子菜单 去掉虚线
        help_menubar = tk.Menu(menubar, tearoff=0)
        help_menubar.add_command(label='关于', command=self.aboutDisp)
        menubar.add_cascade(label='Help', menu=help_menubar)
        self.root['menu'] = menubar

    def inputData(self):
        self.inputPage.grid()
        self.delPage.grid_forget()
        self.updatePage.grid_forget()
        self.countPage.grid_forget()
        self.aboutPage.grid_forget()

    def delData(self):
        self.inputPage.grid_forget()
        self.delPage.grid()
        self.updatePage.grid_forget()
        self.countPage.grid_forget()
        self.aboutPage.grid_forget()

    def updateData(self):
        self.inputPage.grid_forget()
        self.delPage.grid_forget()
        self.updatePage.grid()
        self.countPage.grid_forget()
        self.aboutPage.grid_forget()

    def countData(self):
        self.inputPage.grid_forget()
        self.delPage.grid_forget()
        self.updatePage.grid_forget()
        self.countPage.grid()
        self.aboutPage.grid_forget()

    def aboutDisp(self):
        self.inputPage.grid_forget()
        self.delPage.grid_forget()
        self.updatePage.grid_forget()
        self.countPage.grid_forget()
        self.aboutPage.grid()

    def logoff(self):
        from main import set_up_SIMS
        self.root.destroy()
        set_up_SIMS()

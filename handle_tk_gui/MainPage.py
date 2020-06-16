'''
@Author: randolph
@Date: 2020-06-13 00:12:42
@LastEditors: randolph
@LastEditTime: 2020-06-15 17:30:49
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
from tkinter import *

from view import *


class MainPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        width, height = 770, 360
        self.root.geometry('%dx%d+%d+%d' % (width, height, (self.root.winfo_screenwidth() - width) / 2, (self.root.winfo_screenheight() - height) / 2))
        self.createPage()

    def createPage(self):
        self.inputPage = InputFrame(self.root)      # 创建不同Frame
        self.delPage = DelFrame(self.root)
        self.updatePage = UpdateFrame(self.root)
        self.countPage = CountFrame(self.root)
        self.aboutPage = AboutFrame(self.root)

        self.inputPage.grid()                       # 默认显示录入页面
        menubar = Menu(self.root)
        menubar.add_command(label='录入', command=self.inputData)
        menubar.add_command(label='刪除', command=self.delData)
        menubar.add_command(label='修改', command=self.updateData)
        menubar.add_command(label='报表', command=self.countData)
        menubar.add_command(label='关于', command=self.aboutDisp)
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

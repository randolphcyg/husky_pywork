'''
@Author: randolph
@Date: 2020-06-13 00:11:30
@LastEditors: randolph
@LastEditTime: 2020-06-15 15:39:14
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
from tkinter import *
from tkinter.messagebox import *
from MainPage import *
import tkinter

path = os.getenv('temp')
filename = os.path.join(path, 'pwd.txt')

NAME = 'admin'      # 用户名
PWD = 'admin'       # 密码


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        # 窗口标题
        self.root.title("学生成绩管理系统登录页面")
        # 窗口大小
        width, height = 390, 300
        self.root.geometry('%dx%d+%d+%d' % (width, height, (self.root.winfo_screenwidth() - width) / 2, (self.root.winfo_screenheight() - height) / 2))
        self.root.resizable(0, 0)  # 防止用户调整尺寸
        self.createPage()
        self.auto_fill_pwd()

    def createPage(self):
        self.page = Frame(self.root)        # 创建Frame
        self.page.grid()
        Label(self.page, text="学生成绩信息管理系统", font=24, bg='#6495ED').grid(row=0, column=1, sticky=N, pady=20)

        Label(self.page, text="用户:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=15)
        self.var_name = tkinter.StringVar(self.page, value='')
        self.entry_name = Entry(self.page, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=W, pady=20)

        Label(self.page, text="密码:", font=20).grid(row=2, sticky=E, padx=40, pady=15)
        self.var_pwd = tkinter.StringVar(self.page, value='')
        self.entry_pwd = Entry(self.page, textvariable=self.var_pwd, show='●', width=30)
        self.entry_pwd.grid(row=2, column=1, sticky=W)

        # 选中时变量值为1，未选中时变量值为0，默认选中
        self.remember = tkinter.IntVar(self.page, value=1)
        self.check_remember = tkinter.Checkbutton(self.page, text="记住我？", variable=self.remember, onvalue=1, offvalue=0, font=20)
        self.check_remember.grid(row=4, column=1, sticky=W)

        Button(self.page, text="登录", font=18, bd=3, bg='#7FFFD4', command=self.login).grid(row=5, column=1, sticky=W)
        Button(self.page, text="取消", font=18, bd=3, bg='#F5F5DC', command=self.cancel).grid(row=5, column=1, sticky=N)
        Button(self.page, text="退出", font=18, bd=3, bg='#FF4500', command=self.quit).grid(row=5, column=1, sticky=E)

    def auto_fill_pwd(self):
        '''自动填写用户名密码
        '''
        try:
            with open(filename) as fp:
                _n, _p = fp.read().strip().split(',')
                self.var_name.set(_n)
                self.var_pwd.set(_p)
        except BaseException:
            pass

    def login(self):
        '''登录
        '''
        name = self.entry_name.get()
        pwd = self.entry_pwd.get()
        if name == NAME and pwd == PWD:
            tkinter.messagebox.showinfo(title="恭喜", message="登录成功！")
            self.page.destroy()     # 销毁当前页面
            MainPage(self.root)     # 进入主界面
            if self.remember.get() == 1:
                # 把登录成功的信息写入临时文件
                with open(filename, 'w') as fp:
                    fp.write(','.join((name, pwd)))
            else:
                try:
                    # 删除用于记录用户名和密码的临时文件
                    os.remove(filename)
                except BaseException:
                    pass
        else:
            tkinter.messagebox.showerror("警告！", message="用户名或密码错误")

    def cancel(self):
        '''取消
        '''
        self.var_name.set('')
        self.var_pwd.set('')

    def quit(self):
        '''退出程序
        '''
        self.root.destroy()

import os
import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox
import tkinter.ttk as ttk

from MainPage import MainPage

path = os.getenv('temp')
filename = os.path.join(path, 'pwd.txt')        # 密码文件，不需要自定义

NAME = 'admin'      # 用户名 支持自定义
PWD = 'admin'       # 密码  支持自定义


class LoginPage(object):
    def __init__(self, master=None):
        self.root = master  # 定义内部变量root
        self.root.title("音乐信息管理系统")     # 窗口标题
        # 设置顶级窗体的行列权重，否则子组件的拉伸不会填充整个窗体
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.createPage()
        self.auto_fill_pwd()

    def createPage(self):
        self.page = tk.Frame(self.root, bg='#F5F5F5')        # 创建父Frame
        self.page.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 创建字体 
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 标题
        frm_login = ttk.Frame(self.page, padding=2)
        frm_login.grid(row=0, column=0, columnspan=2, sticky=tk.N)
        self.label_title = tk.Label(frm_login, text="音乐信息管理系统", font=self.ft_title, cursor='circle')
        self.label_title.grid(row=0, column=0, columnspan=2, sticky=tk.N, padx=100, pady=20)
        # 用户行
        frm_user = ttk.Frame(frm_login, padding=2)
        frm_user.grid(row=1, column=0, columnspan=2, sticky=tk.N)
        self.label_user = tk.Label(frm_user, text="用    户:", font=self.ft)
        self.label_user.grid(row=1, column=0, padx=15, pady=10)
        self.var_name = tkinter.StringVar(frm_user, value='')
        self.entry_name = tk.Entry(frm_user, textvariable=self.var_name, font=self.ft, highlightbackground='#708090',
                                   highlightcolor='#3CB371', highlightthickness=2)
        self.entry_name.grid(row=1, column=1, padx=15, pady=10)
        # 密码行
        frm_pwd = ttk.Frame(frm_login, padding=2)
        frm_pwd.grid(row=2, column=0, columnspan=2, sticky=tk.N)
        self.label_pwd = tk.Label(frm_pwd, text="密    码:", font=self.ft)
        self.label_pwd.grid(row=2, column=0, padx=15, pady=10)
        self.var_pwd = tkinter.StringVar(frm_pwd, value='')
        self.entry_pwd = tk.Entry(frm_pwd, textvariable=self.var_pwd, show='●', font=self.ft, highlightbackground='#708090',
                                  highlightcolor='#3CB371', highlightthickness=2)
        self.entry_pwd.grid(row=2, column=1, padx=15, pady=10)
        # 选中时变量值为1，未选中时变量值为0，默认选中
        self.remember = tkinter.IntVar(frm_login, value=1)
        self.check_remember = tkinter.Checkbutton(frm_login, text="记住我？", variable=self.remember, onvalue=1, offvalue=0, font=self.ft)
        self.check_remember.grid(row=3, column=0, columnspan=2, sticky=tk.N, padx=100, pady=10)
        # 控制区第五行放置按钮
        frm_but = ttk.Frame(frm_login, padding=2)
        frm_but.grid(row=4, column=0, columnspan=2, sticky=tk.N)
        tk.Button(frm_but, text="登 录", font=self.ft, bd=3, bg='#87CEFA', command=self.login).grid(row=4, column=1, padx=20, pady=10)
        tk.Button(frm_but, text="清 空", font=self.ft, bd=3, bg='#FFFAF0', command=self.cancel).grid(row=4, column=2, padx=20, pady=10)
        tk.Button(frm_but, text="退 出", font=self.ft, bd=3, bg='#F4A460', command=self.quit).grid(row=4, column=3, padx=20, pady=10)

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

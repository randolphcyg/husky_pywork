'''
@Author: randolph
@Date: 2020-06-02 20:56:28
@LastEditors: randolph
@LastEditTime: 2020-06-13 00:05:12
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 登录窗口
'''
import os
import os.path
import tkinter
import tkinter.messagebox

path = os.getenv('temp')
print(path)
filename = os.path.join(path, 'info.txt')

# 创建应用程序窗口
root = tkinter.Tk()
root.title("学生成绩管理系统登录页面")
# 定义窗口大小
root['height'] = 330
root['width'] = 400
COMMON_F = 16           # 统一字体
COMMON_W = 80           # 统一宽度
COMMON_W_ENTRY = 120    # 输入框统一宽度
COMMON_H = 40           # 统一高度
BUTTON_Y = 260          # 按钮垂直坐标

label_name = tkinter.Label(root, text="用户名:", justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_name.place(x=90, y=60, width=COMMON_W, height=COMMON_H)
var_name = tkinter.StringVar(root, value='')
entry_name = tkinter.Entry(root, width=100, textvariable=var_name)
entry_name.place(x=200, y=60, width=COMMON_W_ENTRY, height=COMMON_H)

label_pwd = tkinter.Label(root, text="密码:", justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_pwd.place(x=90, y=130, width=COMMON_W, height=COMMON_H)
var_pwd = tkinter.StringVar(root, value='')
entry_pwd = tkinter.Entry(root, width=COMMON_W, textvariable=var_pwd, show='*')
entry_pwd.place(x=200, y=130, width=COMMON_W_ENTRY, height=COMMON_H)

try:
    with open(filename) as fp:
        n, p = fp.read().strip().split(',')
        var_name.set(n)
        var_pwd.set(p)
except BaseException:
    pass

# 复选框
rememberMe = tkinter.IntVar(root, value=1)
# 选中时变量值为1，未选中时变量值为0，默认选中
checkRemember = tkinter.Checkbutton(root, text="记住我？", variable=rememberMe, onvalue=1, offvalue=0, font=COMMON_F)
checkRemember.place(x=180, y=180, width=COMMON_W, height=COMMON_H)


def login():
    name = entry_name.get()
    pwd = entry_pwd.get()
    if name == 'admin' and pwd == 'admin':
        tkinter.messagebox.showinfo(title="恭喜", message="登录成功！")
        if rememberMe.get() == 1:
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


# 登录按钮
buttonOk = tkinter.Button(root, text="登录", font=COMMON_F, command=login)
buttonOk.place(x=110, y=250, width=60, height=COMMON_H)


def cancel():
    '''取消
    '''
    var_name.set('')
    var_pwd.set('')


buttonCancel = tkinter.Button(root, text="清空", font=COMMON_F, command=cancel)
buttonCancel.place(x=190, y=250, width=60, height=COMMON_H)


def quit():
    '''退出程序
    '''
    root.destroy()


# 退出按钮
button_confirm = tkinter.Button(root, text="退出", font=COMMON_F, command=quit)
button_confirm.place(x=270, y=250, width=60, height=COMMON_H)

# 启动消息循环
root.mainloop()

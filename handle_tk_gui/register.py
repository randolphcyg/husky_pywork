'''
@Author: randolph
@Date: 2020-06-02 21:34:35
@LastEditors: randolph
@LastEditTime: 2020-06-03 17:45:32
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
import os.path
import re
import tkinter
import tkinter.messagebox

import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(ROOT_PATH, 'student_info.xlsx')
# 创建应用程序窗口
root = tkinter.Tk()
root.title("学生信息登记页面")
root['height'] = 330
root['width'] = 500
COMMON_F = 16           # 统一字体
COMMON_W = 80           # 统一宽度
COMMON_W_ENTRY = 100    # 输入框统一宽度
COMMON_H = 40           # 统一高度
BUTTON_Y = 260          # 按钮垂直坐标
label_header = tkinter.Label(root, text='学生信息登记页面', justify=tkinter.CENTER, anchor='e', font=20)
label_header.place(x=160, y=15, width=180, height=40)
# 第一列
label_name = tkinter.Label(root, text='姓名:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_name.place(x=5, y=60, width=COMMON_W, height=COMMON_H)
var_name = tkinter.StringVar(root, value='')
entry_name = tkinter.Entry(root, width=100, textvariable=var_name)
entry_name.place(x=120, y=60, width=COMMON_W_ENTRY, height=COMMON_H)

label_class = tkinter.Label(root, text='班级:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_class.place(x=5, y=130, width=COMMON_W, height=COMMON_H)
var_class = tkinter.StringVar(root, value='')
entry_class = tkinter.Entry(root, width=COMMON_W, textvariable=var_class)
entry_class.place(x=120, y=130, width=COMMON_W_ENTRY, height=COMMON_H)

label_num = tkinter.Label(root, text='学号:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_num.place(x=5, y=200, width=COMMON_W, height=COMMON_H)
var_num = tkinter.StringVar(root, value='')
entry_num = tkinter.Entry(root, width=COMMON_W, textvariable=var_num)
entry_num.place(x=120, y=200, width=COMMON_W_ENTRY, height=COMMON_H)
# 第二列
label_english = tkinter.Label(root, text='英语:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_english.place(x=250, y=60, width=COMMON_W, height=COMMON_H)
var_english = tkinter.StringVar(root, value='')
entry_english = tkinter.Entry(root, width=COMMON_W, textvariable=var_english)
entry_english.place(x=365, y=60, width=COMMON_W_ENTRY, height=COMMON_H)

label_math = tkinter.Label(root, text='数学:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_math.place(x=250, y=130, width=COMMON_W, height=COMMON_H)
var_math = tkinter.StringVar(root, value='')
entry_math = tkinter.Entry(root, width=COMMON_W, textvariable=var_math)
entry_math.place(x=365, y=130, width=COMMON_W_ENTRY, height=COMMON_H)

label_chinese = tkinter.Label(root, text='语文:', justify=tkinter.RIGHT, anchor='e', width=COMMON_W, font=COMMON_F)
label_chinese.place(x=250, y=200, width=COMMON_W, height=COMMON_H)
var_chinese = tkinter.StringVar(root, value='')
entry_chinese = tkinter.Entry(root, width=COMMON_W, textvariable=var_chinese)
entry_chinese.place(x=365, y=200, width=COMMON_W_ENTRY, height=COMMON_H)


def is_number(num):
    pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
    result = pattern.match(num)
    if result:
        return True
    else:
        return False


def vaild_data():
    '''数据校验逻辑
    '''
    try:
        name = entry_name.get()
        cla = entry_class.get()
        num = entry_num.get()
        english = entry_english.get()
        math = entry_math.get()
        chinese = entry_chinese.get()
        if not num or not name or not cla:
            tkinter.messagebox.showerror('信息', message="姓名班级学号不可为空，请检查输入！")
        elif not is_number(num):
            tkinter.messagebox.showerror('警告', message="学号必须为正整数！请输入正确值！")
        elif not name.isalpha():
            tkinter.messagebox.showerror('警告', message="姓名不合法！请修改后提交！")
        elif not english or not math or not chinese:
            tkinter.messagebox.showerror('信息', message="语数英分数不能为空！请仔细检查！")
        elif not is_number(english):
            tkinter.messagebox.showerror('警告', message="英语分数非法值！请仔细检查！")
        elif not is_number(math):
            tkinter.messagebox.showerror('警告', message="数学分数非法值！请仔细检查！")
        elif not is_number(english):
            tkinter.messagebox.showerror('警告', message="语文分数非法值！请仔细检查！")
        else:
            num = int(num)
            english = float(english)
            math = float(math)
            chinese = float(chinese)

            if english < 0:
                tkinter.messagebox.showerror('警告', message="英语分数不能为负数！请仔细检查！")
            elif math < 0:
                tkinter.messagebox.showerror('警告', message="数学分数不能为负数！请仔细检查！")
            elif chinese < 0:
                tkinter.messagebox.showerror('警告', message="语文分数不能为负数！请仔细检查！")
            elif english > 120:
                tkinter.messagebox.showerror('警告', message="英语分数满分为120！请输入正确值！")
            elif math > 200:
                tkinter.messagebox.showerror('警告', message="数学分数满分为200！请输入正确值！")
            elif chinese > 160:
                tkinter.messagebox.showerror('警告', message="语文分数满分为160！请输入正确值！")
            else:
                return name, cla, num, english, math, chinese
    except Exception as e:
        tkinter.messagebox.showerror('警告', message=e)


def confirm():
    '''确认 保存信息 excel io的处理
    '''
    name, cla, num, english, math, chinese = vaild_data()
    # 写数据之前作已有数据校验
    df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
    row, col = df.shape
    nums_list = df.iloc[:, 2].values.tolist()
    if num in nums_list:
        tar_row = nums_list.index(num)
        df.loc[tar_row] = [name, cla, num, english, math, chinese]
        pd.DataFrame(df).to_excel(output_file, sheet_name='学生信息', header=True, index=False)
        tkinter.messagebox.showinfo(title='信息', message='学生信息登记更新并保存成功！')
    else:
        df.loc[row] = [name, cla, num, english, math, chinese]
        pd.DataFrame(df).to_excel(output_file, sheet_name='学生信息', header=True, index=False)
        tkinter.messagebox.showinfo(title='信息', message='学生信息登记保存成功！')


# 确定按钮
button_confirm = tkinter.Button(root, text='确定', font=COMMON_F, command=confirm)
button_confirm.place(x=90, y=BUTTON_Y, width=COMMON_W, height=COMMON_H)


def cancel():
    '''取消 清空所填信息
    '''
    var_name.set('')
    var_class.set('')
    var_num.set('')
    var_english.set('')
    var_math.set('')
    var_chinese.set('')


# 取消按钮
button_confirm = tkinter.Button(root, text='取消', font=COMMON_F, command=cancel)
button_confirm.place(x=210, y=BUTTON_Y, width=COMMON_W, height=COMMON_H)


def quit():
    '''退出程序
    '''
    root.destroy()


# 退出按钮
button_confirm = tkinter.Button(root, text='退出', font=COMMON_F, command=quit)
button_confirm.place(x=330, y=BUTTON_Y, width=COMMON_W, height=COMMON_H)

if __name__ == "__main__":
    # 文件存在性校验
    is_exist = os.path.exists(output_file)
    if not is_exist:        # 校验表格存在性
        df = pd.DataFrame(columns=["姓名", "班级", "学号", "英语", "数学", "语文"])
        df.to_excel(output_file, encoding='utf-8', sheet_name='学生信息', index=False)
    # 启动消息循环
    root.mainloop()

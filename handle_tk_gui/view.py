'''
@Author: randolph
@Date: 2020-06-13 00:13:19
@LastEditors: randolph
@LastEditTime: 2020-07-03 17:10:37
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 学生信息管理系统各功能页面 
TODO:页面有个显示的小bug需要解决(选完删除菜单再选前面的录入菜单，录入页面的整体会移到最下面)
self.root.resizable(0, 0)  # 防止用户调整尺寸 用这个固定页面防止用户最大化看到bug emm
'''
import os
import re
import tkinter as tk
import tkinter.font as tkf
import tkinter.messagebox
import tkinter.ttk as ttk
from tkinter import Frame  # Frame

import pandas as pd
from PIL import Image, ImageTk

from Tools import Tool

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
temp_file = os.path.join(ROOT_PATH, 'temp.xlsx')
output_file = os.path.join(ROOT_PATH, 'student_info.xlsx')
pic = os.path.join(ROOT_PATH, 'randolph.jpg')


class InputFrame(Frame):                # 继承 Frame 类
    '''信息输入页面类
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Tool = Tool()       # 初始化工具类
        self.Tool.check_file()               # 校验表格文件
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self)        # 创建父Frame
        self.page.grid(sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 字体
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 嵌套区域
        self.frm_input = ttk.Frame(self.page, padding=2)
        self.frm_input.grid(row=0, column=0, columnspan=4, sticky=tk.N)
        # 标题
        self.label_title = tk.Label(self.frm_input, text="信息录入页面", font=self.ft_title, cursor='mouse')
        self.label_title.grid(row=0, column=0, columnspan=4, sticky=tk.N, padx=100, pady=10)
        # 用户行
        frm_content = ttk.Frame(self.frm_input, padding=2)
        frm_content.grid(columnspan=4, sticky=tk.N)
        self.label_name = tk.Label(frm_content, text="姓    名:", font=self.ft)
        self.label_name.grid(row=1, column=0, sticky=tk.E, padx=40, pady=10)

        self.var_name = tkinter.StringVar(frm_content, value='')
        self.entry_name = tk.Entry(frm_content, textvariable=self.var_name, width=20)
        self.entry_name.grid(row=1, column=1, sticky=tk.W, pady=10)

        self.label_num = tk.Label(frm_content, text="学    号:", font=self.ft)
        self.label_num.grid(row=1, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_num = tkinter.StringVar(frm_content, value='')
        self.entry_num = tk.Entry(frm_content, textvariable=self.var_num, width=20)
        self.entry_num.grid(row=1, column=3, sticky=tk.W, pady=10)
        # 第二行
        self.label_cla = tk.Label(frm_content, text="班    级:", font=self.ft)
        self.label_cla.grid(row=2, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_cla = tkinter.StringVar(frm_content, value='')
        self.entry_cla = tk.Entry(frm_content, textvariable=self.var_cla, width=20)
        self.entry_cla.grid(row=2, column=1, sticky=tk.W, pady=10)

        self.label_gender = tk.Label(frm_content, text="性    别:", font=self.ft)
        self.label_gender.grid(row=2, column=2, sticky=tk.E, padx=40, pady=10)
        # 下拉菜单
        self.cmb = ttk.Combobox(frm_content, width=3)
        self.cmb.grid(row=2, column=3, sticky=tk.W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        self.label_sub1 = tk.Label(frm_content, text="大学语文:", font=self.ft)
        self.label_sub1.grid(row=3, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub1 = tkinter.StringVar(frm_content, value='')
        self.entry_sub1 = tk.Entry(frm_content, textvariable=self.var_sub1, width=20)
        self.entry_sub1.grid(row=3, column=1, sticky=tk.W)

        self.label_sub2 = tk.Label(frm_content, text="高等数学:", font=self.ft)
        self.label_sub2.grid(row=3, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub2 = tkinter.StringVar(frm_content, value='')
        self.entry_sub2 = tk.Entry(frm_content, textvariable=self.var_sub2, width=20)
        self.entry_sub2.grid(row=3, column=3, sticky=tk.W)
        # 第四行
        self.label_sub3 = tk.Label(frm_content, text="线性代数:", font=self.ft)
        self.label_sub3.grid(row=4, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub3 = tkinter.StringVar(frm_content, value='')
        self.entry_sub3 = tk.Entry(frm_content, textvariable=self.var_sub3, width=20)
        self.entry_sub3.grid(row=4, column=1, sticky=tk.W)

        self.label_sub4 = tk.Label(frm_content, text="大学英语:", font=self.ft)
        self.label_sub4.grid(row=4, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub4 = tkinter.StringVar(frm_content, value='')
        self.entry_sub4 = tk.Entry(frm_content, textvariable=self.var_sub4, width=20)
        self.entry_sub4.grid(row=4, column=3, sticky=tk.W)
        # 第五行
        self.label_sub5 = tk.Label(frm_content, text="Python开发:", font=self.ft)
        self.label_sub5.grid(row=5, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub5 = tkinter.StringVar(frm_content, value='')
        self.entry_sub5 = tk.Entry(frm_content, textvariable=self.var_sub5, width=20)
        self.entry_sub5.grid(row=5, column=1, sticky=tk.W)

        self.label_sub6 = tk.Label(frm_content, text="大学体育:", font=self.ft)
        self.label_sub6.grid(row=5, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub6 = tkinter.StringVar(frm_content, value='')
        self.entry_sub6 = tk.Entry(frm_content, textvariable=self.var_sub6, width=20)
        self.entry_sub6.grid(row=5, column=3, sticky=tk.W)
        # 第六行
        frm_but = ttk.Frame(self.page, padding=2)
        frm_but.grid(row=6, column=0, columnspan=4, sticky=tk.N)
        self.but_save = tk.Button(frm_but, text="保 存", font=self.ft, bd=3, bg='#87CEFA', command=self.save)
        self.but_save.grid(row=6, column=1, padx=20, pady=10, sticky=tk.W)
        self.but_cancel = tk.Button(frm_but, text="清 空", font=self.ft, bd=3, bg='#F5F5DC', command=self.cancel)
        self.but_cancel.grid(row=6, column=2, padx=20, pady=10, sticky=tk.N)

    def vaild_data(self):
        '''数据校验逻辑
        '''
        try:
            num = self.var_num.get()
            name = self.var_name.get()
            cla = self.var_cla.get()
            gender = self.cmb.get()
            sub1 = self.var_sub1.get()
            sub2 = self.var_sub2.get()
            sub3 = self.var_sub3.get()
            sub4 = self.var_sub4.get()
            sub5 = self.var_sub5.get()
            sub6 = self.var_sub6.get()
            if not num or not name or not cla:
                tkinter.messagebox.showerror("信息", message="姓名班级学号不可为空，请检查输入！")
            elif not self.Tool.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.Tool.is_number(sub1) or not self.Tool.is_number(sub2) or not self.Tool.is_number(sub3) or \
            not self.Tool.is_number(sub4) or not self.Tool.is_number(sub5) or not self.Tool.is_number(sub6):
                tkinter.messagebox.showerror("警告", message="各学科分数存在非法值！请仔细检查！")
            else:
                num = int(num)
                # 成绩转换为浮点类型
                sub1, sub2, sub3, sub4, sub5, sub6 = float(sub1), float(sub2), float(sub3), float(sub4), float(sub5), float(sub6)
                if sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 or sub6 < 0:
                    tkinter.messagebox.showerror("警告", message="各学科分数不能为负数！请仔细检查！")
                elif sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100 or sub6 > 100:
                    tkinter.messagebox.showerror("警告", message="各学科分数满分为100！请输入正确值！")
                else:
                    return num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6
        except Exception as e:
            tkinter.messagebox.showerror("警告", message=e)

    def save(self):
        '''保存信息
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = self.vaild_data()
        # 写数据之前作已有数据校验
        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        nums_list = df.iloc[:, 0].values.tolist()       # 先查出学号，判断改学生是否已经存数据
        if num in nums_list:
            tar_row = nums_list.index(num)
            df.loc[tar_row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记更新并保存成功！")
        else:
            df.loc[row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记保存成功！")

    def cancel(self):
        '''清空
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.cmb.current(0)     # 下拉框恢复
        self.var_sub1.set('')
        self.var_sub2.set('')
        self.var_sub3.set('')
        self.var_sub4.set('')
        self.var_sub5.set('')
        self.var_sub6.set('')


class DelFrame(Frame):
    '''信息删除页面类
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self)        # 创建父Frame
        self.page.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 字体
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 嵌套区域
        self.frm_del = ttk.Frame(self.page, padding=2)
        self.frm_del.grid(row=0, column=0, columnspan=4, sticky=tk.N)
        # 标题
        self.label_title = tk.Label(self.frm_del, text="信息查询删除页面", font=self.ft_title, cursor='cross')
        self.label_title.grid(row=0, column=0, columnspan=4, sticky=tk.N, padx=100, pady=10)
        # 用户行
        frm_content = ttk.Frame(self.frm_del, padding=2)
        frm_content.grid(columnspan=4, sticky=tk.N)
        self.label_name = tk.Label(frm_content, text="姓    名:", font=self.ft)
        self.label_name.grid(row=1, column=0, sticky=tk.E, padx=40, pady=10)

        self.var_name = tkinter.StringVar(frm_content, value='')
        self.entry_name = tk.Entry(frm_content, textvariable=self.var_name, width=20)
        self.entry_name.grid(row=1, column=1, sticky=tk.W, pady=10)

        self.label_num = tk.Label(frm_content, text="学    号:", font=self.ft)
        self.label_num.grid(row=1, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_num = tkinter.StringVar(frm_content, value='')
        self.entry_num = tk.Entry(frm_content, textvariable=self.var_num, width=20)
        self.entry_num.grid(row=1, column=3, sticky=tk.W, pady=10)
        # # 第二行
        self.label_cla_title = tk.Label(frm_content, text="班    级:", font=self.ft)
        self.label_cla_title.grid(row=2, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_cla = tkinter.StringVar(frm_content, value='')
        self.label_cla = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_cla)
        self.label_cla.grid(row=2, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_gender_title = tk.Label(frm_content, text="性    别:", font=self.ft)
        self.label_gender_title.grid(row=2, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_gender = tkinter.StringVar(frm_content, value='')
        self.label_gender = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_gender)
        self.label_gender.grid(row=2, column=3, sticky=tk.W, padx=40, pady=10)
        # # 第三行
        self.label_sub1_title = tk.Label(frm_content, text="大学语文:", font=self.ft)
        self.label_sub1_title.grid(row=3, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub1 = tkinter.StringVar(frm_content, value='')
        self.label_sub1 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub1)
        self.label_sub1.grid(row=3, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_sub2_title = tk.Label(frm_content, text="高等数学:", font=self.ft)
        self.label_sub2_title.grid(row=3, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub2 = tkinter.StringVar(frm_content, value='')
        self.label_sub2 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub2)
        self.label_sub2.grid(row=3, column=3, sticky=tk.W, padx=40, pady=10)
        # # 第四行
        self.label_sub3_title = tk.Label(frm_content, text="线性代数:", font=self.ft)
        self.label_sub3_title.grid(row=4, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub3 = tkinter.StringVar(frm_content, value='')
        self.label_sub3 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub3)
        self.label_sub3.grid(row=4, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_sub4_title = tk.Label(frm_content, text="大学英语:", font=self.ft)
        self.label_sub4_title.grid(row=4, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub4 = tkinter.StringVar(frm_content, value='')
        self.label_sub4 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub4)
        self.label_sub4.grid(row=4, column=3, sticky=tk.W, padx=40, pady=10)
        # # 第五行
        self.label_sub5_title = tk.Label(frm_content, text="Python开发:", font=self.ft)
        self.label_sub5_title.grid(row=5, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub5 = tkinter.StringVar(frm_content, value='')
        self.label_sub5 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub5)
        self.label_sub5.grid(row=5, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_sub6_title = tk.Label(frm_content, text="大学体育:", font=self.ft)
        self.label_sub6_title.grid(row=5, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub6 = tkinter.StringVar(frm_content, value='')
        self.label_sub6 = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_sub6)
        self.label_sub6.grid(row=5, column=3, sticky=tk.W, padx=40, pady=10)
        # 第六行
        frm_but = ttk.Frame(self.page, padding=2)
        frm_but.grid(row=6, column=0, columnspan=4, sticky=tk.N)
        self.but_fetch = tk.Button(frm_but, text="查 询", font=self.ft, bd=3, bg='#87CEFA', command=self.fetch)
        self.but_fetch.grid(row=6, column=0, padx=20, pady=10, sticky=tk.W)
        self.but_del = tk.Button(frm_but, text="删 除", font=self.ft, bd=3, bg='#FFC0CB', command=self.delete)
        self.but_del.grid(row=6, column=1, padx=20, pady=10, sticky=tk.N)
        self.but_cancel = tk.Button(frm_but, text="清 空", font=self.ft, bd=3, bg='#F5F5DC', command=self.cancel)
        self.but_cancel.grid(row=6, column=2, padx=20, pady=10, sticky=tk.E)

    def fetch(self):
        '''先查询出信息，再去删除
        用学号或姓名查询
        '''
        num = self.var_num.get()
        name = self.var_name.get()        # 先不根据名字搜索，如果有重名情况，则提示需要输入学号辅助判断
        self.cancel()
        if num and name:
            num = int(num)          # 注意输入的学号都要转成int类型才能用
            self.var_num.set(num)
            self.var_name.set(name)
        elif num:
            num = int(num)
            self.var_num.set(num)
        elif name:
            self.var_name.set(name)

        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        names_list = df.iloc[:, 1].values.tolist()      # 姓名列表
        nums_list = df.iloc[:, 0].values.tolist()       # 学号列表
        name_exist_time = names_list.count(name)        # 姓名出现的次数：0次没有此人，1次仅有一个，1个以上需学号查询

        if name:            # 先根据姓名查询
            if name_exist_time == 0:
                tkinter.messagebox.showinfo(title="警告", message="查无此人！")
            elif name_exist_time == 1:
                tar_row = names_list.index(name)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)
            elif name_exist_time != 1:
                tkinter.messagebox.showinfo(title="提示", message="存在重名！请输入学号辅助判断")
        elif num:           # 再根据学号查
            if num in nums_list:
                tar_row = nums_list.index(num)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)

    def fill_table(self, data_list):
        '''将查询值塞回界面
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = data_list
        self.var_num.set(num)
        self.var_name.set(name)
        self.var_cla.set(cla)
        self.var_gender.set(gender)
        self.var_sub1.set(sub1)
        self.var_sub2.set(sub2)
        self.var_sub3.set(sub3)
        self.var_sub4.set(sub4)
        self.var_sub5.set(sub5)
        self.var_sub6.set(sub6)

    def delete(self):
        '''用学号或姓名搜到一个人然后删除
        还可以优化运行速度和判断逻辑
        '''
        name = self.var_name.get()
        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        names_list = df.iloc[:, 1].values.tolist()      # 姓名列表
        nums_list = df.iloc[:, 0].values.tolist()       # 学号列表
        name_exist_time = names_list.count(name)        # 姓名出现的次数：0次没有此人，1次仅有一个，1个以上需学号查询

        self.fetch()                    # 先搜索信息返回页面
        cla = self.var_cla.get()        # 用班级信息去判断是否fetch到信息
        if cla:
            num = self.var_num.get()
            if name:            # 先根据姓名查询
                if name_exist_time == 0:
                    tkinter.messagebox.showinfo(title="警告", message="查无此人！")
                elif name_exist_time == 1:
                    tar_row = names_list.index(name)
                    df.drop(tar_row, inplace=True)              # 删除相应行
                    self.update_csv_file(df)                    # 更新csv文件
                elif name_exist_time != 1:
                    tkinter.messagebox.showinfo(title="提示", message="存在重名！请输入学号辅助判断")
            elif num:           # 再根据学号查
                if num in nums_list:
                    tar_row = nums_list.index(num)
                    df.drop(tar_row, inplace=True)              # 删除相应行
                    self.update_csv_file(df)                    # 更新csv文件
        else:
            tkinter.messagebox.showinfo(title="提示", message="未查询到此人信息！请先检查学号姓名并点击【查询】按钮核实信息")
        pass

    def update_csv_file(self, df):
        confirm = tkinter.messagebox.askokcancel('提示', "确定删除此人信息？")
        if confirm:
            # 打开临时csv文件将df写入temp_file临时文件
            df_header = pd.DataFrame(columns=["学号", "姓名", "班级", "性别", "大学语文", "高等数学",
                                              "线性代数", "大学英语", "Python开发", "大学体育"])
            df_header.to_excel(temp_file, encoding='utf-8', sheet_name="学生信息", index=False)     # 写头信息
            pd.DataFrame(df).to_excel(temp_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息删除成功！")
            os.remove(output_file)                  # 删除源文件
            os.rename(temp_file, output_file)       # 临时文件修改名字
            self.cancel()                           # 清空界面信息
        else:
            pass

    def cancel(self):
        '''清空
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.var_gender.set('')
        self.var_sub1.set('')
        self.var_sub2.set('')
        self.var_sub3.set('')
        self.var_sub4.set('')
        self.var_sub5.set('')
        self.var_sub6.set('')


class UpdateFrame(Frame):
    '''信息更新页面类
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.Tool = Tool()       # 初始化工具类
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self)        # 创建父Frame
        self.page.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 字体
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 嵌套区域
        self.frm_update = ttk.Frame(self.page, padding=2)
        self.frm_update.grid(row=0, column=0, columnspan=4, sticky=tk.N)
        # 标题
        self.label_title = tk.Label(self.frm_update, text="信息查询修改页面", font=self.ft_title, cursor='mouse')
        self.label_title.grid(row=0, column=0, columnspan=4, sticky=tk.N, padx=100, pady=10)
        # 用户行
        frm_content = ttk.Frame(self.frm_update, padding=2)
        frm_content.grid(columnspan=4, sticky=tk.N)
        self.label_name = tk.Label(frm_content, text="姓    名:", font=self.ft)
        self.label_name.grid(row=1, column=0, sticky=tk.E, padx=40, pady=10)

        self.var_name = tkinter.StringVar(frm_content, value='')
        self.entry_name = tk.Entry(frm_content, textvariable=self.var_name, width=20)
        self.entry_name.grid(row=1, column=1, sticky=tk.W, pady=10)

        self.label_num = tk.Label(frm_content, text="学    号:", font=self.ft)
        self.label_num.grid(row=1, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_num = tkinter.StringVar(frm_content, value='')
        self.entry_num = tk.Entry(frm_content, textvariable=self.var_num, width=20)
        self.entry_num.grid(row=1, column=3, sticky=tk.W, pady=10)
        # 第二行
        self.label_cla = tk.Label(frm_content, text="班    级:", font=self.ft)
        self.label_cla.grid(row=2, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_cla = tkinter.StringVar(frm_content, value='')
        self.entry_cla = tk.Entry(frm_content, textvariable=self.var_cla, width=20)
        self.entry_cla.grid(row=2, column=1, sticky=tk.W, pady=10)

        self.label_gender = tk.Label(frm_content, text="性    别:", font=self.ft)
        self.label_gender.grid(row=2, column=2, sticky=tk.E, padx=40, pady=10)
        # 下拉菜单
        self.cmb = ttk.Combobox(frm_content, width=3)
        self.cmb.grid(row=2, column=3, sticky=tk.W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        self.label_sub1 = tk.Label(frm_content, text="大学语文:", font=self.ft)
        self.label_sub1.grid(row=3, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub1 = tkinter.StringVar(frm_content, value='')
        self.entry_sub1 = tk.Entry(frm_content, textvariable=self.var_sub1, width=20)
        self.entry_sub1.grid(row=3, column=1, sticky=tk.W)

        self.label_sub2 = tk.Label(frm_content, text="高等数学:", font=self.ft)
        self.label_sub2.grid(row=3, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub2 = tkinter.StringVar(frm_content, value='')
        self.entry_sub2 = tk.Entry(frm_content, textvariable=self.var_sub2, width=20)
        self.entry_sub2.grid(row=3, column=3, sticky=tk.W)
        # 第四行
        self.label_sub3 = tk.Label(frm_content, text="线性代数:", font=self.ft)
        self.label_sub3.grid(row=4, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub3 = tkinter.StringVar(frm_content, value='')
        self.entry_sub3 = tk.Entry(frm_content, textvariable=self.var_sub3, width=20)
        self.entry_sub3.grid(row=4, column=1, sticky=tk.W)

        self.label_sub4 = tk.Label(frm_content, text="大学英语:", font=self.ft)
        self.label_sub4.grid(row=4, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub4 = tkinter.StringVar(frm_content, value='')
        self.entry_sub4 = tk.Entry(frm_content, textvariable=self.var_sub4, width=20)
        self.entry_sub4.grid(row=4, column=3, sticky=tk.W)
        # 第五行
        self.label_sub5 = tk.Label(frm_content, text="Python开发:", font=self.ft)
        self.label_sub5.grid(row=5, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_sub5 = tkinter.StringVar(frm_content, value='')
        self.entry_sub5 = tk.Entry(frm_content, textvariable=self.var_sub5, width=20)
        self.entry_sub5.grid(row=5, column=1, sticky=tk.W)

        self.label_sub6 = tk.Label(frm_content, text="大学体育:", font=self.ft)
        self.label_sub6.grid(row=5, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_sub6 = tkinter.StringVar(frm_content, value='')
        self.entry_sub6 = tk.Entry(frm_content, textvariable=self.var_sub6, width=20)
        self.entry_sub6.grid(row=5, column=3, sticky=tk.W)
        # 第六行
        frm_but = ttk.Frame(self.page, padding=2)
        frm_but.grid(row=6, column=0, columnspan=4, sticky=tk.N)
        self.but_fetch = tk.Button(frm_but, text="查 询", font=self.ft, bd=3, bg='#87CEFA', command=self.fetch)
        self.but_fetch.grid(row=6, column=0, padx=20, pady=10, sticky=tk.W)
        self.but_save = tk.Button(frm_but, text="保 存", font=self.ft, bd=3, bg='#FFC0CB', command=self.update)
        self.but_save.grid(row=6, column=1, padx=20, pady=10, sticky=tk.N)
        self.but_cancel = tk.Button(frm_but, text="清 空", font=self.ft, bd=3, bg='#F5F5DC', command=self.cancel)
        self.but_cancel.grid(row=6, column=2, padx=20, pady=10, sticky=tk.E)

    def fetch(self):
        '''先查询出信息，再去修改
        用学号或姓名查询
        '''
        num = self.var_num.get()
        name = self.var_name.get()        # 先不根据名字搜索，如果有重名情况，则提示需要输入学号辅助判断

        self.cancel()
        if num and name:
            num = int(num)          # 注意输入的学号都要转成int类型才能用
            self.var_num.set(num)
            self.var_name.set(name)
        elif num:
            num = int(num)
            self.var_num.set(num)
        elif name:
            self.var_name.set(name)

        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        names_list = df.iloc[:, 1].values.tolist()      # 姓名列表
        nums_list = df.iloc[:, 0].values.tolist()       # 学号列表
        name_exist_time = names_list.count(name)        # 姓名出现的次数：0次没有此人，1次仅有一个，1个以上需学号查询

        if name:            # 先根据姓名查询
            if name_exist_time == 0:
                tkinter.messagebox.showinfo(title="警告", message="查无此人！")
            elif name_exist_time == 1:
                tar_row = names_list.index(name)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)
            elif name_exist_time != 1:
                tkinter.messagebox.showinfo(title="提示", message="存在重名！请输入学号辅助判断")
        elif num:           # 再根据学号查
            if num in nums_list:
                tar_row = nums_list.index(num)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)

    def fill_table(self, data_list):
        '''将查询值塞回界面
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = data_list
        self.var_num.set(num)
        self.var_name.set(name)
        self.var_cla.set(cla)
        if gender == "男":
            self.cmb.current(0)
        else:
            self.cmb.current(1)
        self.var_sub1.set(sub1)
        self.var_sub2.set(sub2)
        self.var_sub3.set(sub3)
        self.var_sub4.set(sub4)
        self.var_sub5.set(sub5)
        self.var_sub6.set(sub6)

    def vaild_data(self):
        '''数据校验逻辑
        '''
        try:
            num = self.var_num.get()
            name = self.var_name.get()
            cla = self.var_cla.get()
            gender = self.cmb.get()
            sub1 = self.var_sub1.get()
            sub2 = self.var_sub2.get()
            sub3 = self.var_sub3.get()
            sub4 = self.var_sub4.get()
            sub5 = self.var_sub5.get()
            sub6 = self.var_sub6.get()
            if not num or not name or not cla:
                tkinter.messagebox.showerror("信息", message="姓名班级学号不可为空，请检查输入！")
            elif not self.Tool.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.Tool.is_number(sub1) or not self.Tool.is_number(sub2) or not self.Tool.is_number(sub3) or \
             not self.Tool.is_number(sub4) or not self.Tool.is_number(sub5) or not self.Tool.is_number(sub6):
                tkinter.messagebox.showerror("警告", message="各学科分数存在非法值！请仔细检查！")
            else:
                num = int(num)
                # 成绩转换为浮点类型
                sub1, sub2, sub3, sub4, sub5, sub6 = float(sub1), float(sub2), float(sub3), float(sub4), float(sub5), float(sub6)

                if sub1 < 0 or sub2 < 0 or sub3 < 0 or sub4 < 0 or sub5 < 0 or sub6 < 0:
                    tkinter.messagebox.showerror("警告", message="各学科分数不能为负数！请仔细检查！")
                elif sub1 > 100 or sub2 > 100 or sub3 > 100 or sub4 > 100 or sub5 > 100 or sub6 > 100:
                    tkinter.messagebox.showerror("警告", message="各学科分数满分为100！请输入正确值！")
                else:
                    return num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6
        except Exception as e:
            tkinter.messagebox.showerror("警告", message=e)

    def update(self):
        '''保存修改信息
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = self.vaild_data()
        # 写数据之前作已有数据校验
        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        nums_list = df.iloc[:, 0].values.tolist()       # 先查出学号，判断改学生是否已经存数据
        if num in nums_list:
            tar_row = nums_list.index(num)
            df.loc[tar_row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
            pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
            tkinter.messagebox.showinfo(title="信息", message="学生信息登记更新并保存成功！")
        else:
            confirm = tkinter.messagebox.askokcancel('提示', "确定修改学号？")
            if confirm:
                df.loc[row] = [num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6]
                pd.DataFrame(df).to_excel(output_file, sheet_name="学生信息", header=True, index=False)
                tkinter.messagebox.showinfo(title="信息", message="学生信息登记保存成功！")
            else:
                pass

    def cancel(self):
        '''清空
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.cmb.current(0)     # 下拉框恢复
        self.var_sub1.set('')
        self.var_sub2.set('')
        self.var_sub3.set('')
        self.var_sub4.set('')
        self.var_sub5.set('')
        self.var_sub6.set('')


class CountFrame(Frame):
    '''报表页面类
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self)        # 创建父Frame
        self.page.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 字体
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 嵌套区域
        self.frm_count = ttk.Frame(self.page, padding=2)
        self.frm_count.grid(row=0, column=0, columnspan=4, sticky=tk.N)
        # 标题
        self.label_title = tk.Label(self.frm_count, text="学生信息报表页面", font=self.ft_title, cursor='mouse')
        self.label_title.grid(row=0, column=0, columnspan=4, sticky=tk.N, padx=100, pady=10)
        # 用户行
        frm_content = ttk.Frame(self.frm_count, padding=2)
        frm_content.grid(columnspan=4, sticky=tk.N)
        self.label_name = tk.Label(frm_content, text="姓    名:", font=self.ft)
        self.label_name.grid(row=1, column=0, sticky=tk.E, padx=40, pady=10)

        self.var_name = tkinter.StringVar(frm_content, value='')
        self.entry_name = tk.Entry(frm_content, textvariable=self.var_name, width=20)
        self.entry_name.grid(row=1, column=1, sticky=tk.W, pady=10)

        self.label_num = tk.Label(frm_content, text="学    号:", font=self.ft)
        self.label_num.grid(row=1, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_num = tkinter.StringVar(frm_content, value='')
        self.entry_num = tk.Entry(frm_content, textvariable=self.var_num, width=20)
        self.entry_num.grid(row=1, column=3, sticky=tk.W, pady=10)
        # 第二行
        self.label_cla_title = tk.Label(frm_content, text="班    级:", font=self.ft)
        self.label_cla_title.grid(row=2, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_cla = tkinter.StringVar(frm_content, value='')
        self.label_cla = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_cla)
        self.label_cla.grid(row=2, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_evaluation_title = tk.Label(frm_content, text="总    评:", font=self.ft)
        self.label_evaluation_title.grid(row=2, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_evaluation = tkinter.StringVar(frm_content, value='')
        self.label_evaluation = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_evaluation)
        self.label_evaluation.grid(row=2, column=3, sticky=tk.W, padx=40, pady=10)
        # 第三行
        self.label_failed_sub_count_title = tk.Label(frm_content, text="不及格:", font=self.ft)
        self.label_failed_sub_count_title.grid(row=3, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_failed_sub_count = tkinter.StringVar(frm_content, value='')
        self.label_failed_sub_count = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_failed_sub_count)
        self.label_failed_sub_count.grid(row=3, column=1, sticky=tk.W, padx=40, pady=10)
        # 第四行
        self.label_fair_sub_count_title = tk.Label(frm_content, text="中    等:", font=self.ft)
        self.label_fair_sub_count_title.grid(row=4, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_fair_sub_count = tkinter.StringVar(frm_content, value='')
        self.label_fair_sub_count = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_fair_sub_count)
        self.label_fair_sub_count.grid(row=4, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_good_sub_count_title = tk.Label(frm_content, text="良    好:", font=self.ft)
        self.label_good_sub_count_title.grid(row=4, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_good_sub_count = tkinter.StringVar(frm_content, value='')
        self.label_good_sub_count = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_good_sub_count)
        self.label_good_sub_count.grid(row=4, column=3, sticky=tk.W, padx=40, pady=10)
        # 第五行
        self.label_excellent_sub_count_title = tk.Label(frm_content, text="优    秀:", font=self.ft)
        self.label_excellent_sub_count_title.grid(row=5, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_excellent_sub_count = tkinter.StringVar(frm_content, value='')
        self.label_excellent_sub_count = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_excellent_sub_count)
        self.label_excellent_sub_count.grid(row=5, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_gpa_title = tk.Label(frm_content, text="绩    点:", font=self.ft)
        self.label_gpa_title.grid(row=5, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_gpa = tkinter.StringVar(frm_content, value='')
        self.label_gpa = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_gpa)
        self.label_gpa.grid(row=5, column=3, sticky=tk.W, padx=40, pady=10)

        # 第六行
        self.label_average_grade_title = tk.Label(frm_content, text="平均成绩:", font=self.ft)
        self.label_average_grade_title.grid(row=6, column=0, sticky=tk.E, padx=40, pady=10)
        self.var_average_grade = tkinter.StringVar(frm_content, value='')
        self.label_average_grade = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_average_grade)
        self.label_average_grade.grid(row=6, column=1, sticky=tk.W, padx=40, pady=10)

        self.label_total_grade_title = tk.Label(frm_content, text="总成绩:", font=self.ft).grid(row=6, column=2, sticky=tk.E, padx=40, pady=10)
        self.var_total_grade = tkinter.StringVar(frm_content, value='')
        self.label_total_grade = tk.Label(frm_content, text="", font=self.ft, textvariable=self.var_total_grade)
        self.label_total_grade.grid(row=6, column=3, sticky=tk.W, padx=40, pady=10)
        # 第七行
        frm_but = ttk.Frame(self.page, padding=2)
        frm_but.grid(row=7, column=0, columnspan=4, sticky=tk.N)
        self.but_fetch_count = tk.Button(frm_but, text="查询报表", font=self.ft, bd=3, bg='#87CEFA', command=self.fetch)
        self.but_fetch_count.grid(row=7, column=0, padx=40, pady=10, sticky=tk.W)
        self.but_cancel = tk.Button(frm_but, text="清 空", font=self.ft, bd=3, bg='#F5F5DC', command=self.cancel)
        self.but_cancel.grid(row=7, column=1, padx=40, pady=10, sticky=tk.E)

    def fetch(self):
        '''根据学号或姓名查询并返回成绩报表
        '''
        num = self.var_num.get()
        name = self.var_name.get()        # 先不根据名字搜索，如果有重名情况，则提示需要输入学号辅助判断
        self.cancel()
        if num and name:
            num = int(num)          # 注意输入的学号都要转成int类型才能用
            self.var_num.set(num)
            self.var_name.set(name)
        elif num:
            num = int(num)
            self.var_num.set(num)
        elif name:
            self.var_name.set(name)

        df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
        row, col = df.shape
        names_list = df.iloc[:, 1].values.tolist()      # 姓名列表
        nums_list = df.iloc[:, 0].values.tolist()       # 学号列表
        name_exist_time = names_list.count(name)        # 姓名出现的次数：0次没有此人，1次仅有一个，1个以上需学号查询

        if name:            # 先根据姓名查询
            if name_exist_time == 0:
                tkinter.messagebox.showinfo(title="警告", message="查无此人！")
            elif name_exist_time == 1:
                tar_row = names_list.index(name)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)
            elif name_exist_time != 1:
                tkinter.messagebox.showinfo(title="提示", message="存在重名！请输入学号辅助判断")
        elif num:           # 再根据学号查
            if num in nums_list:
                tar_row = nums_list.index(num)
                fetch_data_list = df.loc[tar_row].tolist()
                self.fill_table(fetch_data_list)

    def gpa_standard(self, sub_list):
        '''标准gpa计算改进4.0(2)版本算法
        '''
        res = 0
        for sub in sub_list:
            if 75 >= sub >= 60:
                res += 2
            if 85 >= sub >= 75:
                res += 3
            if sub > 85:
                res += 4
        return round(res / len(sub_list), 2)

    def fill_table(self, data_list):
        '''将查询值塞回界面 textvariable
        '''
        num, name, cla, gender, sub1, sub2, sub3, sub4, sub5, sub6 = data_list
        sub_list = [sub1, sub2, sub3, sub4, sub5, sub6]
        failed_sub_count = 0
        fair_sub_count = 0
        good_sub_count = 0
        excellent_sub_count = 0
        # course_credit_list = [2, 6, 4, 3, 3, 2]         # 课程学分列表(自定义) 先不管课程学分
        gpa = self.gpa_standard(sub_list)
        average_grade = 0
        total_grade = 0
        # 根据返回成绩计算数据
        for sub in sub_list:
            total_grade += sub
            if sub < 60:
                failed_sub_count += 1
            if 75 >= sub >= 60:
                fair_sub_count += 1
            if 85 >= sub >= 75:
                good_sub_count += 1
            if sub > 85:
                excellent_sub_count += 1
        average_grade = round(total_grade / len(sub_list), 1)          # 四舍五入
        # 总评计算
        evaluation = ""
        if gpa < 1:
            evaluation = "不及格"
        elif 2.5 > gpa >= 1:
            evaluation = "及格"
        elif 3.5 > gpa >= 2.5:
            evaluation = "中等"
        elif 3.7 > gpa >= 3.5:
            evaluation = "良好"
        elif gpa >= 3.7:
            evaluation = "优秀"

        self.var_num.set(num)
        self.var_name.set(name)
        self.var_cla.set(cla)
        self.var_evaluation.set(evaluation)                                 # 总评
        self.var_failed_sub_count.set(str(failed_sub_count) + " 科")        # 不及格科目数
        self.var_fair_sub_count.set(str(fair_sub_count) + " 科")            # 中等科目数
        self.var_good_sub_count.set(str(good_sub_count) + " 科")            # 良好科目数
        self.var_excellent_sub_count.set(str(excellent_sub_count) + " 科")  # 优等科目数
        self.var_gpa.set(gpa)                                               # 绩点
        self.var_average_grade.set(average_grade)                           # 平均成绩
        self.var_total_grade.set(total_grade)                               # 总成绩

    def cancel(self):
        '''清空
        '''
        self.var_num.set('')
        self.var_name.set('')
        self.var_cla.set('')
        self.var_evaluation.set('')             # 总评
        self.var_failed_sub_count.set('')       # 不及格科目数
        self.var_fair_sub_count.set('')         # 中等科目数
        self.var_good_sub_count.set('')         # 良好科目数
        self.var_excellent_sub_count.set('')    # 优等科目数
        self.var_gpa.set('')                    # 绩点
        self.var_average_grade.set('')          # 平均成绩
        self.var_total_grade.set('')            # 总成绩


class AboutFrame(Frame):
    '''关于页面类
    '''
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createPage()

    def createPage(self):
        self.page = tk.Frame(self)        # 创建父Frame
        self.page.grid(row=0, column=0, sticky=tk.NSEW)
        # 设置继承类MWindow的行列权重，保证内建子组件会拉伸填充
        self.page.rowconfigure(0, weight=1)
        self.page.columnconfigure(0, weight=1)
        # 字体
        self.ft_title = tkf.Font(family='微软雅黑', size=16)    # 标题字体
        self.ft = tkf.Font(family='微软雅黑', size=12)          # 普通字体
        # 嵌套区域
        self.frm_about = ttk.LabelFrame(self.page, padding=2, text='关于学生信息管理系统')
        self.frm_about.grid(row=0, column=0, columnspan=4, sticky=tk.N)

        self.about_text = "【使用说明】\n\n1. 此次tkinter实践主要难点在于tkinter本身的页面跳转设计\n\n采用登录进来后子tab页面的设计\n\n2. 优点在于用pandas处理csv数据比较高效简便\n\n3. 涉及的点有学号作为唯一ID，其他数据有空值、非法值校验\n\n4. 查询可先输入姓名查询，若有多个重名，再补充学号即可\n\n5. 在报表功能中有设计对GPA的简单计算"
        self.var_about = tkinter.StringVar(self, value=self.about_text)
        tk.Label(self.frm_about, text="", font=self.ft, justify=tk.LEFT, textvariable=self.var_about).grid(row=1, column=0, sticky=tk.W, padx=40, pady=10)
        # label插入图像 遵循grid布局
        self.load = Image.open(pic)
        self.render = ImageTk.PhotoImage(self.load)
        self.label_img = tk.Label(self.frm_about, image=self.render)
        self.label_img.grid(row=1, column=1, sticky=tk.W)
        # 嵌套区域二
        labelsFrame = ttk.LabelFrame(self.frm_about, text=' About Randoph ')
        labelsFrame.grid(column=0, row=8, columnspan=4)

        self.label_des1 = tk.Label(labelsFrame, font=self.ft, text="Minecraft是我的理想")
        self.label_des1.grid(column=0, row=0)
        self.label_des2 = tk.Label(labelsFrame, font=self.ft, text="向往着自由 向往着缤纷浪漫的生活")
        self.label_des2.grid(column=0, row=1, sticky=tk.W)

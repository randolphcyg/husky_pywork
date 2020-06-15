'''
@Author: randolph
@Date: 2020-06-13 00:13:19
@LastEditors: randolph
@LastEditTime: 2020-06-15 16:24:08
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
import os.path
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

import pandas as pd
from PIL import Image, ImageTk

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
temp_file = os.path.join(ROOT_PATH, 'temp.xlsx')
output_file = os.path.join(ROOT_PATH, 'student_info.xlsx')
pic = os.path.join(ROOT_PATH, 'randolph.jpg')


class InputFrame(Frame):                # 继承Frame类
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master              # 定义内部变量root
        self.itemName = StringVar()
        self.importPrice = StringVar()
        self.sellPrice = StringVar()
        self.deductPrice = StringVar()
        self.createPage()

    def createPage(self):
        # 文件存在性校验
        self.is_exist = os.path.exists(output_file)
        if not self.is_exist:        # 校验表格存在性
            df = pd.DataFrame(columns=["学号", "姓名", "班级", "性别", "大学语文", "高等数学",
                                       "线性代数", "大学英语", "Python开发", "大学体育"])
            df.to_excel(output_file, encoding='utf-8', sheet_name="学生信息", index=False)

        Label(self, text="信息录入页面", font=24, bg='#6A5ACD').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="姓名:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=W)

        Label(self, text="学号:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=3, sticky=W, pady=20)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.entry_cla = Entry(self, textvariable=self.var_cla, width=30)
        self.entry_cla.grid(row=2, column=1, sticky=W, pady=20)

        Label(self, text="性别:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        # 下拉菜单
        self.cmb = ttk.Combobox(self)
        self.cmb.grid(row=2, column=3, sticky=W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        Label(self, text="大学语文:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_sub1 = tkinter.StringVar(self, value='')
        self.entry_sub1 = Entry(self, textvariable=self.var_sub1, width=30)
        self.entry_sub1.grid(row=3, column=1, sticky=W)

        Label(self, text="高等数学:", font=20).grid(row=3, column=2, sticky=E, padx=40, pady=5)
        self.var_sub2 = tkinter.StringVar(self, value='')
        self.entry_sub2 = Entry(self, textvariable=self.var_sub2, width=30)
        self.entry_sub2.grid(row=3, column=3, sticky=W)
        # 第四行
        Label(self, text="线性代数:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_sub3 = tkinter.StringVar(self, value='')
        self.entry_sub3 = Entry(self, textvariable=self.var_sub3, width=30)
        self.entry_sub3.grid(row=4, column=1, sticky=W)

        Label(self, text="大学英语:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_sub4 = tkinter.StringVar(self, value='')
        self.entry_sub4 = Entry(self, textvariable=self.var_sub4, width=30)
        self.entry_sub4.grid(row=4, column=3, sticky=W)
        # 第五行
        Label(self, text="Python开发:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_sub5 = tkinter.StringVar(self, value='')
        self.entry_sub5 = Entry(self, textvariable=self.var_sub5, width=30)
        self.entry_sub5.grid(row=5, column=1, sticky=W)

        Label(self, text="大学体育:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_sub6 = tkinter.StringVar(self, value='')
        self.entry_sub6 = Entry(self, textvariable=self.var_sub6, width=30)
        self.entry_sub6.grid(row=5, column=3, sticky=W)
        # 第六行
        Button(self, text="保存", font=18, bd=3, bg='#22c9c9', command=self.save).grid(row=6, column=1, sticky=W)
        Button(self, text="清空", font=18, bd=3, bg='#F5F5DC', command=self.cancel).grid(row=6, column=1, sticky=N)
        Button(self, text="退出", font=18, bd=3, bg='#FF4500', command=self.quit).grid(row=6, column=1, sticky=E)

    def quit(self):
        '''退出程序
        '''
        self.root.destroy()

    def is_number(self, num):
        pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
        result = pattern.match(num)
        if result:
            return True
        else:
            return False

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
            elif not self.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.is_number(sub1) or not self.is_number(sub2) or not self.is_number(sub3) or not self.is_number(sub4) or not self.is_number(sub5) or not self.is_number(sub6):
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
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text="信息查询删除页面", font=24, bg='#FF7F50').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="姓名:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=W)

        Label(self, text="学号:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=3, sticky=W, pady=20)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_cla).grid(row=2, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="性别:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        self.var_gender = tkinter.StringVar(self, value='')
        self.label_gender = Label(self, text="", font=20, textvariable=self.var_gender).grid(row=2, column=3, sticky=W, padx=40, pady=5)
        # 第三行
        Label(self, text="大学语文:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_sub1 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub1).grid(row=3, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="高等数学:", font=20).grid(row=3, column=2, sticky=E, padx=40, pady=5)
        self.var_sub2 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub2).grid(row=3, column=3, sticky=W, padx=40, pady=5)
        # 第四行
        Label(self, text="线性代数:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_sub3 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub3).grid(row=4, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="大学英语:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_sub4 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub4).grid(row=4, column=3, sticky=W, padx=40, pady=5)
        # 第五行
        Label(self, text="Python开发:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_sub5 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub5).grid(row=5, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="大学体育:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_sub6 = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_sub6).grid(row=5, column=3, sticky=W, padx=40, pady=5)
        # 第六行
        Button(self, text="查询", font=18, bd=3, bg='#22c9c9', command=self.fetch).grid(row=6, column=1, sticky=W)
        Button(self, text="删除", font=18, bd=3, bg='#FFC0CB', command=self.delete).grid(row=6, column=1, sticky=N)
        Button(self, text="清空", font=18, bd=3, bg='#F5F5DC', command=self.cancel).grid(row=6, column=1, sticky=E)

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
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.itemName = StringVar()
        self.createPage()

    def createPage(self):
        Label(self, text="信息查询修改页面", font=24, bg='#D8BFD8').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="姓名:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=W)

        Label(self, text="学号:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=3, sticky=W, pady=20)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.entry_cla = Entry(self, textvariable=self.var_cla, width=30)
        self.entry_cla.grid(row=2, column=1, sticky=W, pady=20)

        Label(self, text="性别:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        # 下拉菜单
        self.cmb = ttk.Combobox(self)
        self.cmb.grid(row=2, column=3, sticky=W)
        self.cmb['value'] = ("男", "女")
        self.cmb.current(0)
        # 第三行
        Label(self, text="大学语文:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_sub1 = tkinter.StringVar(self, value='')
        self.entry_sub1 = Entry(self, textvariable=self.var_sub1, width=30)
        self.entry_sub1.grid(row=3, column=1, sticky=W)

        Label(self, text="高等数学:", font=20).grid(row=3, column=2, sticky=E, padx=40, pady=5)
        self.var_sub2 = tkinter.StringVar(self, value='')
        self.entry_sub2 = Entry(self, textvariable=self.var_sub2, width=30)
        self.entry_sub2.grid(row=3, column=3, sticky=W)
        # 第四行
        Label(self, text="线性代数:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_sub3 = tkinter.StringVar(self, value='')
        self.entry_sub3 = Entry(self, textvariable=self.var_sub3, width=30)
        self.entry_sub3.grid(row=4, column=1, sticky=W)

        Label(self, text="大学英语:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_sub4 = tkinter.StringVar(self, value='')
        self.entry_sub4 = Entry(self, textvariable=self.var_sub4, width=30)
        self.entry_sub4.grid(row=4, column=3, sticky=W)
        # 第五行
        Label(self, text="Python开发:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_sub5 = tkinter.StringVar(self, value='')
        self.entry_sub5 = Entry(self, textvariable=self.var_sub5, width=30)
        self.entry_sub5.grid(row=5, column=1, sticky=W)

        Label(self, text="大学体育:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_sub6 = tkinter.StringVar(self, value='')
        self.entry_sub6 = Entry(self, textvariable=self.var_sub6, width=30)
        self.entry_sub6.grid(row=5, column=3, sticky=W)
        # 第六行
        Button(self, text="查询", font=18, bd=3, bg='#22c9c9', command=self.fetch).grid(row=6, column=1, sticky=W)
        Button(self, text="保存", font=18, bd=3, bg='#4682B4', command=self.update).grid(row=6, column=1, sticky=N)
        Button(self, text="清空", font=18, bd=3, bg='#F5F5DC', command=self.cancel).grid(row=6, column=1, sticky=E)

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

    def is_number(self, num):
        '''正则判断是否为数字串
        '''
        pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
        result = pattern.match(num)
        if result:
            return True
        else:
            return False

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
            elif not self.is_number(num):
                tkinter.messagebox.showerror("警告", message="学号必须为正整数！请输入正确值！")
            elif not name.isalpha():
                tkinter.messagebox.showerror("警告", message="姓名不合法！请修改后提交！")
            elif not sub1 or not sub2 or not sub3 or not sub4 or not sub4 or not sub5 or not sub6:
                tkinter.messagebox.showerror("信息", message="各学科分数不能为空！请仔细检查！")
            elif not self.is_number(sub1) or not self.is_number(sub2) or not self.is_number(sub3) or not self.is_number(sub4) or not self.is_number(sub5) or not self.is_number(sub6):
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
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text="报表页面", font=24, bg='#DDA0DD').grid(row=0, column=1, sticky=N, pady=10)
        # 第一行
        Label(self, text="姓名:", font=20).grid(row=1, column=0, sticky=E, padx=40, pady=5)
        self.var_name = tkinter.StringVar(self, value='')
        self.entry_name = Entry(self, textvariable=self.var_name, width=30)
        self.entry_name.grid(row=1, column=1, sticky=W)

        Label(self, text="学号:", font=20).grid(row=1, column=2, sticky=E, padx=40, pady=5)
        self.var_num = tkinter.StringVar(self, value='')
        self.entry_num = Entry(self, textvariable=self.var_num, width=30)
        self.entry_num.grid(row=1, column=3, sticky=W, pady=20)
        # 第二行
        Label(self, text="班级:", font=20).grid(row=2, column=0, sticky=E, padx=40, pady=5)
        self.var_cla = tkinter.StringVar(self, value='')
        self.label_cla = Label(self, text="", font=20, textvariable=self.var_cla).grid(row=2, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="总评:", font=20).grid(row=2, column=2, sticky=E, padx=40, pady=5)
        self.var_evaluation = tkinter.StringVar(self, value='')
        self.label_evaluation = Label(self, text="", font=20, textvariable=self.var_evaluation).grid(row=2, column=3, sticky=W, padx=40, pady=5)
        # 第三行
        Label(self, text="不及格:", font=20).grid(row=3, column=0, sticky=E, padx=40, pady=5)
        self.var_failed_sub_count = tkinter.StringVar(self, value='')
        self.label_failed_sub_count = Label(self, text="", font=20, textvariable=self.var_failed_sub_count).grid(row=3, column=1, sticky=W, padx=40, pady=5)

        # 第四行
        Label(self, text="中等:", font=20).grid(row=4, column=0, sticky=E, padx=40, pady=5)
        self.var_fair_sub_count = tkinter.StringVar(self, value='')
        self.label_fair_sub_count = Label(self, text="", font=20, textvariable=self.var_fair_sub_count).grid(row=4, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="良好:", font=20).grid(row=4, column=2, sticky=E, padx=40, pady=5)
        self.var_good_sub_count = tkinter.StringVar(self, value='')
        self.label_good_sub_count = Label(self, text="", font=20, textvariable=self.var_good_sub_count).grid(row=4, column=3, sticky=W, padx=40, pady=5)
        # 第五行
        Label(self, text="优秀:", font=20).grid(row=5, column=0, sticky=E, padx=40, pady=5)
        self.var_excellent_sub_count = tkinter.StringVar(self, value='')
        self.label_excellent_sub_count = Label(self, text="", font=20, textvariable=self.var_excellent_sub_count).grid(row=5, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="绩点:", font=20).grid(row=5, column=2, sticky=E, padx=40, pady=5)
        self.var_gpa = tkinter.StringVar(self, value='')
        self.label_gpa = Label(self, text="", font=20, textvariable=self.var_gpa).grid(row=5, column=3, sticky=W, padx=40, pady=5)

        # 第六行
        Label(self, text="平均成绩:", font=20).grid(row=6, column=0, sticky=E, padx=40, pady=5)
        self.var_average_grade = tkinter.StringVar(self, value='')
        self.label_average_grade = Label(self, text="", font=20, textvariable=self.var_average_grade).grid(row=6, column=1, sticky=W, padx=40, pady=5)

        Label(self, text="总成绩:", font=20).grid(row=6, column=2, sticky=E, padx=40, pady=5)
        self.var_total_grade = tkinter.StringVar(self, value='')
        self.label_total_grade = Label(self, text="", font=20, textvariable=self.var_total_grade).grid(row=6, column=3, sticky=W, padx=40, pady=5)

        # 第七行
        Button(self, text="查询报表", font=18, bd=3, bg='#22c9c9', command=self.fetch).grid(row=7, column=1, sticky=W)
        Button(self, text="清空", font=18, bd=3, bg='#F5F5DC', command=self.cancel).grid(row=7, column=1, sticky=E)

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
                sub * 4
        average_grade = round(total_grade / len(sub_list), 1)          # 四舍五入
        # 总评计算
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
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.root = master
        self.createPage()

    def createPage(self):
        Label(self, text="关于", font=24, bg='#00FFFF').grid(row=0, column=0, sticky=N, pady=10)
        # 嵌套区域一
        self.LF = ttk.LabelFrame(self, text='关于学生信息管理系统')
        self.LF.grid(column=0, row=0, padx=8, pady=4)

        self.about_text = "【使用说明】\n\n1. 此次tkinter实践主要难点在于tkinter本身的页面跳转设计\n\n采用登录进来后子tab页面的设计\n\n2. 优点在于用pandas处理csv数据比较高效简便\n\n3. 涉及的点有学号作为唯一ID，其他数据有空值、非法值校验\n\n4. 查询可先输入姓名查询，若有多个重名，再补充学号即可\n\n5. 在报表功能中有设计对GPA的简单计算"
        self.var_about = tkinter.StringVar(self, value=self.about_text)
        Label(self.LF, text="", font=20, justify=LEFT, textvariable=self.var_about).grid(row=1, column=0, sticky=W, padx=40, pady=5)
        # label插入图像 遵循grid布局
        self.load = Image.open(pic)
        self.render = ImageTk.PhotoImage(self.load)
        Label(self.LF, image=self.render).grid(row=1, column=1, sticky=W)
        # 嵌套区域二
        labelsFrame = ttk.LabelFrame(self.LF, text=' About Randoph ')
        labelsFrame.grid(column=0, row=8, columnspan=4)

        ttk.Label(labelsFrame, font=16, text="Minecraft是我的理想").grid(column=0, row=0)
        ttk.Label(labelsFrame, font=16, text="向往着自由 向往着缤纷浪漫的生活").grid(column=0, row=1, sticky=W)

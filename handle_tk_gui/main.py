'''
@Author: randolph
@Date: 2020-06-13 00:10:32
@LastEditors: randolph
@LastEditTime: 2020-06-15 16:42:50
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
import os.path
from tkinter import *

from PIL import Image, ImageTk

from LoginPage import *

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
ico = os.path.join(ROOT_PATH, 'randolph.ico')

root = Tk()
LoginPage(root)
# 设置图标
load = Image.open(ico)
img = ImageTk.PhotoImage(load)
root.tk.call('wm', 'iconphoto', root._w, img)

root.mainloop()

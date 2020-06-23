'''
@Author: randolph
@Date: 2020-06-23 18:14:22
@LastEditors: randolph
@LastEditTime: 2020-06-23 18:23:08
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 处理txt的模板，若遇到关于txt的问题，建议将基础的功能封装成模块
'''
import os

import numpy as np
import pandas as pd

FILE_NAME = 'srctest.txt'
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
SRC_FILE = os.path.join(ROOT_PATH, FILE_NAME)


# 按行读取文件
with open(SRC_FILE, mode='rt', encoding='utf-8') as src_file:
    clear_src_file = [x.strip() for x in src_file if x.strip() != '']       # 去换行符和空格
    for i, line in enumerate(clear_src_file):
        # left_word_str = line.split(':')[0]
        print(i + 1, line)

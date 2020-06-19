'''
@Author: randolph
@Date: 2020-06-18 09:50:12
@LastEditors: randolph
@LastEditTime: 2020-06-19 12:16:28
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import os
import re

import pandas as pd

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(ROOT_PATH, 'student_info.xlsx')


class Tool():
    '''工具类
    '''
    def __init__(self):
        pass

    def is_number(self, num):
        '''判断字符串是否为数字
        '''
        pattern = re.compile(r'^[-+]?[-0-9]\d*\.\d*|[-+]?\.?[0-9]\d*$')
        result = pattern.match(num)
        if result:
            return True
        else:
            return False

    def check_file(self):
        '''文件存在性校验
        '''
        self.is_exist = os.path.exists(output_file)
        if not self.is_exist:        # 校验表格存在性
            df = pd.DataFrame(columns=["学号", "姓名", "班级", "性别", "大学语文", "高等数学",
                                       "线性代数", "大学英语", "Python开发", "大学体育"])
            df.to_excel(output_file, encoding='utf-8', sheet_name="学生信息", index=False)

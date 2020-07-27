'''
@Author: randolph
@Date: 2020-06-04 18:36:36
@LastEditors: randolph
@LastEditTime: 2020-06-05 10:39:18
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 处理字符串，split join filter format方法使用
'''
import os

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
IN_FILE = os.path.join(ROOT_PATH, 'listin.txt')
OUT_FILE = os.path.join(ROOT_PATH, 'listout.txt')


def cust_format(n):
    with open(IN_FILE, mode='rt', encoding='utf-8') as in_file, \
            open(OUT_FILE, mode='wt', encoding='utf-8') as out_file:
        clear_in_file = [x.strip() for x in in_file if x.strip() != '']
        for i, line in enumerate(clear_in_file):
            # 冒号左边字符串处理
            left_word_str = line.split(':')[0]
            left_word_list = list(filter(None, left_word_str.split(" ")))   # 用filter过滤一个或多个空格
            left_word_str_res = ' '.join(left_word_list)                    # 单词以空格为间隔拼接为字符串
            if len(left_word_str_res) > n - 2:
                print("冒号插入位置过小！请调整大一些")
            else:
                left_word_str_res_format = left_word_str_res.ljust(n - 1)           # 字符串右侧补充空格到n-1位
                left_word_str_res_format_insert = left_word_str_res_format + ':'    # 左边字符串补冒号，此时冒号就在第n个位置上
                # 右边字符串处理
                right_word_str = line.split(':')[1]
                right_word_list = list(filter(None, right_word_str.split(" ")))     # 过滤空格
                right_word_str_res = ' '.join(right_word_list)
                res_line = '{0} {1}'.format(left_word_str_res_format_insert, right_word_str_res)    # 左右字符串加空格
                print(res_line)
                out_file.write(res_line + '\n')     # 写入文件并换行


if __name__ == "__main__":
    risk_local_str = input("请输入大于冒号左边长度的正整数:\n")
    if risk_local_str.isdigit():
        risk_local = int(risk_local_str)
        cust_format(risk_local)
    else:
        print("请检查是否输入非整数！")

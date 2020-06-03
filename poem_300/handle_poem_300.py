#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author: randolph
@Date: 2020-06-01 23:58:59
@LastEditors: randolph
@LastEditTime: 2020-06-03 14:09:43
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 用jieba处理唐诗三百首作业
'''
import logging
import re
from collections import Counter

import jieba        # 处理自然语言库
import jieba.posseg as pseg

jieba.setLogLevel(logging.INFO)     # 提升jieba日志级别 关闭jieba debug日志输出
jieba.initialize()                  # 手动初始化jieba 加快调用函数速度

POEM_FILE = 'e:/randolph/husky_pywork/poem_300/poem.txt'        # 古诗词源文件路径


def route(ori_data):
    '''函数入口判断
    '''
    flag = input('')
    if flag == '作者':
        n = int(input(''))
        count_authors(ori_data, n)              # 统计作者姓名频次
    elif flag == '人物':
        n = int(input(''))
        count_names(n)                          # 统计人物姓名频次
    elif flag == '唐诗':
        count_poems(ori_data)                   # 统计唐诗数量
        exit()                                  # 结束
    elif flag == '飞花':
        s = str(input(''))
        poem_rhythm(ori_data, key_character=s)  # 输出飞花令诗句
    elif flag.isdigit() and len(flag) == 3:
        show_poem(flag)                         # 输出对应编号古诗
    else:
        print('输入错误')
        exit()          # 结束
    route(ori_data)     # 每次输入完成将重新回到主路由


def read_poem_file(path):
    '''读取文件去除换行符，转换为列表
    '''
    with open(path, mode='r', encoding='utf-8') as poem_file:
        content = poem_file.readlines()
        clear_content_list = [x.strip() for x in content if x.strip() != '']      # 去除换行符、空字符
        return clear_content_list


def count_authors(data, n):
    '''统计作者及频次排行
    应网友要求，不用正则匹配，也可以获取全量作者
    第一个for循环中，注释了的三行和接下来的两行代码效果相同
    '''
    authors_list = []
    sen = []
    for item in data:
        # if bool(re.search(r'\d', item)):                    # 搜索包含数字的行
        #     local = re.findall(r'\d{3}(.+?) ', item)        # 惰性匹配
        #     authors_list.append(local[0])

        # 将字符串空格去掉后，判断是否全为字符，不全是字符，则说明包含数字，则取到数字和作者这行
        if not item.replace(' ', '').isalpha():
            authors_list.append(item.split(' ')[0][3:])  # 用空格切分字符串后从第三个字符取导最后即为姓名

    result = Counter(authors_list)                          # 统计列表元素
    sort_result = sorted(result.items(), key=lambda x: x[1], reverse=True)      # 排序
    for author in sort_result[:n]:
        author_info = list(author)
        print(author_info[0], author_info[1])


def show_poem(flag):
    '''根据编号展示整首古诗 格式不变
    '''
    with open(POEM_FILE, mode='r', encoding='utf-8') as poem_file:
        content = poem_file.read()
        # 第一种正则匹配方式 精确
        # if len(str(int(flag))) == 2:
        #     flag_plus = str(int(flag)+1).zfill(3)
        # else:
        #     flag_plus = str(int(flag)+1)
        # pattern1 = str(flag) + '(.*)' + flag_plus
        # 第二种匹配方式 灵活简单
        pattern2 = str(flag) + r'(.+?)\d{3}'    # 其余通用匹配
        pattern3 = str(flag) + r'(.+?)$'        # 320特殊情况
        if flag != '320':
            local = re.findall(pattern2, content, re.S)[0]  # re.S 匹配换行符 支持多行匹配
            print(local.split(' \n\n')[0])      # 去除诗末空格和俩换行
        else:
            local = re.findall(pattern3, content, re.S)[0]
            print(local)


def count_poems(data):
    '''计算古诗数量
    '''
    poems_list = []
    for item in data:
        if bool(re.search(r'\d', item)):
            local = re.findall(r'\d{3}(.+?) ', item)        # 惰性匹配
            poems_list.append(local[0])
    print(len(poems_list))


def poem_rhythm(data, key_character):
    '''飞花令 长度不超过7个字
    '''
    new_poem_lines_list = []
    for item in data:
        if not bool(re.search(r'\d', item)):        # 排除诗名
            for line in item.split(' '):            # 诗句每行根据空格拆成诗句
                new_poem_lines_list.append(line)

    for line in new_poem_lines_list:
        if key_character in line and len(line.replace(' ', '')) <= 7:
            print(line)


def count_names(n):
    '''统计全文范围内的中文姓名及频次
    '''
    with open(POEM_FILE, mode='r', encoding='utf-8') as poem_file:
        # 先获取作者列表
        data = read_poem_file(POEM_FILE)
        authors_list = []
        for item in data:
            if bool(re.search(r'\d', item)):                    # 搜索包含数字的行
                local = re.findall(r'\d{3}(.+?) ', item)        # 惰性匹配
                authors_list.append(local[0])
        # 然后全文范围内处理
        content = poem_file.read()
        names_list = []
        # 切词
        words = pseg.cut(content)
        for w in words:
            if w.flag == 'nr' and 1 < len(w.word) and w.word in authors_list:
                names_list.append(w.word)
        # 统计姓名列表
        result = Counter(names_list)
        sort_result = sorted(result.items(), key=lambda x: x[1], reverse=True)      # 排序
        # 只打印n条信息
        for name in sort_result[:n]:
            name_info = list(name)
            print(name_info[0], name_info[1])


if __name__ == "__main__":
    ori_data_list = read_poem_file(POEM_FILE)
    route(ori_data_list)
    # count_authors(ori_data_list, 5)       # 不用正则取作者测试    通过√

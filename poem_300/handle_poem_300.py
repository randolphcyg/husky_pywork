#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author: randolph
@Date: 2020-06-01 23:58:59
@LastEditors: randolph
@LastEditTime: 2020-06-02 09:58:09
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 用jieba处理唐诗三百首作业
'''
import re
import jieba
from collections import Counter
POEM_FILE = 'e:/randolph/husky_pywork/poem_300/poem.txt'
STOP_FILE = 'e:/randolph/husky_pywork/poem_300/stopwords.txt'


def route(ori_data):
    '''函数入口判断
    '''
    flag = input('')
    if flag == '作者':
        n = int(input(''))
        count_authors(ori_data, flag, n)
    elif flag == '人物':
        n = int(input(''))
        count_names(ori_data, flag, n)
    elif flag == '唐诗':
        count_poems(ori_data)   # 统计唐诗数量
        exit()          # 结束
    elif flag == '飞花':
        s = str(input(''))
        poem_rhythm(ori_data, key_character=s)
    elif flag.isdigit() and len(flag) == 3:
        show_poem(flag)
    else:
        print('输入错误')


def read_poem_file(path):
    '''读取文件去除换行符，转换为列表
    '''
    with open(path, mode='r', encoding='utf-8') as poem_file:
        content = poem_file.readlines()
        # clear_content_list = [x.strip('\n') for x in content]
        clear_content_list = [x.strip() for x in content if x.strip() != '']      # 去除换行符、空字符
        return clear_content_list


def count_authors(data, flag, n):
    '''统计作者及频次排行
    '''
    authors_list = []
    for item in data:
        if bool(re.search(r'\d', item)):        # 搜索包含数字的行
            local = re.findall(r'\d{3}(.+?) ', item)        # 惰性匹配
            authors_list.append(local[0])
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
        # 第二种匹配方式 简单
        pattern2 = str(flag) + r'(.+?)\d{3}'
        local = re.findall(pattern2, content, re.S)[0]  # re.S 匹配换行符 支持多行匹配
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


def count_names(data, flag, n):
    '''统计全文范围内的中文姓名及频次
    '''
    pass


if __name__ == "__main__":
    ori_data_list = read_poem_file(POEM_FILE)
    route(ori_data_list)
    # show_poem('084')
    # count_poems(ori_data_list)
    # poem_rhythm(ori_data_list, '秦')
    # count_authors(ori_data_list, '作者', 10)

#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os  # 文件/目录
import re  # 正则
import time  # 时间处理
from functools import wraps  # 装饰器

import matplotlib.pyplot as plt  # 2D绘图
import numpy as np  # 数据处理
import pandas as pd  # 数据处理
import requests  # 处理http请求
from bs4 import BeautifulSoup  # 爬虫库

# 设置中文字体和负号正常显示
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# 定义全局常量
ROOT_PATH = os.path.dirname(os.path.abspath(__file__))          # 当前程序文件所在的绝对路径
EXCEL = os.path.join(ROOT_PATH, 'gucheng_stock_info.xls')       # 存储股票信息的表格文件位置
STOCK_LIST_URL = 'https://hq.gucheng.com/gpdmylb.html'          # 股城网-行情-股票代码一览表 用于获取股票代码
STOCK_INFO_URL = 'https://hq.gucheng.com/'                      # 股城网-行情-首页 用于单支股票url拼接


def menu():
    '''菜单,展示功能菜单，提供用户选择
    '''
    print('''
    ╔———————股票爬虫&可视化系统————————————————————╗
    │                                              │
    │   =============== 功能菜单 ===============   │
    │                                              │
    │   1. 爬取股票信息                            │
    │                                              │
    │   2. 展示股票信息                            │
    │                                              │
    │   3. 股票可视化——饼图                        │
    │                                              │
    │   4. 股票可视化——柱状图                      │
    │                                              │
    │   5. 股票可视化——雷达图                      │
    │                                              │
    │   6. 删除旧股票信息文件                      │
    │                                              │
    │   0. 退出系统                                │
    │                                              │
    │  ==========================================  │
    │  说明:通过数字选择菜单,例输入0回车则退出系统 │
    ╚——————————————————————————————————————————————╝
    ''')


def main():
    '''主函数,根据用户输入数字运行不同功能
    '''
    ctrl = True  # 标记是否退出系统
    while (ctrl):
        menu()  # 显示菜单
        option = re.sub(r"\D", "", input("请选择:"))    # 选择菜单项，提取数字
        options = [str(x) for x in list(range(7))]      # 选择列表
        if option in options:
            option_int = int(option)
            if option_int == 0:     # 退出系统
                print('退出股票爬虫&可视化系统！')
                ctrl = False
            elif option_int == 1:   # 爬取股票信息
                max_num = int(input("期望获取的股票支数:"))
                print('爬虫运行中...')
                stock_code_list = get_stock_list()
                get_stock_info(stock_code_list[:max_num])
            elif option_int == 2:   # 展示股票信息
                res = read_excel()
                print(res)
            elif option_int == 3:   # 股票可视化——饼图
                draw_pie()
            elif option_int == 4:   # 股票可视化——柱状图
                draw_histogram()
            elif option_int == 5:   # 股票可视化——雷达图
                draw_radar()
            elif option_int == 6:   # 删除旧股票信息文件
                del_excel()


def del_excel():
    '''删除文件
    '''
    is_exist = os.path.exists(EXCEL)
    if is_exist:
        os.remove(EXCEL)                  # 删除源文件
    print("删除旧股票表格文件成功!")


def read_excel():
    '''读取源文件
    '''
    df = pd.read_excel(EXCEL, encoding='utf-8', error_bad_lines=False, converters={'股票代码': str})
    return df


def func_timer(function):
    '''计时器
    '''
    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} 开始...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} 结束, 耗时: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result
    return function_timer


def getHTMLText(url, code="utf-8"):
    '''获取HTML文本
    '''
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = code
        return r.text
    except Exception as e:
        print('当前错误:' + str(e))
        return ""


@func_timer
def get_stock_list():
    '''获取股票代码列表
    '''
    html = getHTMLText(STOCK_LIST_URL, "GB2312")
    soup = BeautifulSoup(html, 'html.parser')
    a_list = soup.find_all('a')      # 得到一个列表
    stock_code_list = []
    for content in a_list:
        try:
            href = content.attrs['href']      # 股票代码都存放在href标签中
            stock_code_list.append(re.findall(r"[S][HZ]\d{6}", href)[0])
        except Exception as e:
            print('当前错误:' + str(e))
            continue
    return stock_code_list


@func_timer
def get_stock_info(lst):
    '''获取单支股票信息
    '''
    count = 0
    for index, stock in enumerate(lst):
        url = STOCK_INFO_URL + stock + "/"  # url为单只股票的url
        html = getHTMLText(url)  # 爬取单只股票网页，得到HTML
        try:
            if html == "":      # 爬取失败，则继续爬取下一只股票
                continue
            info_dict = {}       # 字典存储单只股票信息
            soup = BeautifulSoup(html, 'html.parser')       # 单只股票页面用BeautifulSoup处理
            stockInfo = soup.find('div', attrs={'class': 'stock_top clearfix'})
            # 在观察股城网时发现，单只股票信息都存放在div的'class':'stock_top clearfix'中
            # 在soup中找到所有标签div中属性为'class':'stock_top clearfix'的内容
            name = stockInfo.find_all(attrs={'class': 'stock_title'})[0]
            # 在stockInfo中找到存放有股票名称和代码的'stock_title'标签
            info_dict["股票代码"] = name.text.split("\n")[2]
            info_dict.update({'股票名称': name.text.split("\n")[1]})
           # 对name以换行进行分割，得到一个列表，第1项为股票名称，第2项为代码
           # 如果以空格股票名称中包含空格，会产生异常，
           # 如“万 科A",得到股票名称为万，代码为科A
            key_list = stockInfo.find_all('dt')
            value_list = stockInfo.find_all('dd')
            # 股票信息都存放在dt和dd标签中，用find_all产生列表
            for i in range(len(key_list)):
                key = key_list[i].text
                val = value_list[i].text
                info_dict[key] = val
                # 将信息的名称和值作为键值对，存入字典中
            print(index, info_dict)
            save_info(info_dict)    # 保存单支股票信息
            count = count + 1
            print("\r爬取单支股票成功，当前进度: {:.2f}%\n".format(count * 100 / len(lst)), end="")
        except Exception as e:
            print('当前错误:' + str(e))
            count = count + 1
            print("\r爬取单支股票失败，当前进度: {:.2f}%\n".format(count * 100 / len(lst)), end="")
            continue


def save_info(info_dict):
    '''会将新爬取的股票信息存入表格中，重复出现的股票也会重复添加；
    因此可先执行删除表格文件，再爬取股票信息存储；
    '''
    # 表格文件存在校验
    is_exist = os.path.exists(EXCEL)
    title = ['股票代码', '股票名称', '最高', '最低', '今开', '昨收', '涨停', '跌停', '换手率', '振幅',
             '成交量', '成交额', '内盘', '外盘', '委比', '涨跌幅', '市盈率(动)', '市净率', '流通市值', '总市值']
    if not is_exist:
        df = pd.DataFrame(columns=title)
        df.to_excel(EXCEL, encoding='utf-8', sheet_name="stocks", index=False)

    # 读取源文件
    df = pd.read_excel(EXCEL, encoding='utf-8', error_bad_lines=False, converters={'股票代码': str})
    row, col = df.shape     # 表格文件现有行列数目
    df.loc[row] = [info_dict['股票代码'],
                   info_dict['股票名称'],
                   info_dict['最高'],
                   info_dict['最低'],
                   info_dict['今开'],
                   info_dict['昨收'],
                   info_dict['涨停'],
                   info_dict['跌停'],
                   info_dict['换手率'],
                   info_dict['振幅'],
                   info_dict['成交量'],
                   info_dict['成交额'],
                   info_dict['内盘'],
                   info_dict['外盘'],
                   info_dict['量比'],
                   info_dict['涨跌幅'],
                   info_dict['市盈率(动)'],
                   info_dict['市净率'],
                   info_dict['流通市值'],
                   info_dict['总市值']]
    pd.DataFrame(df).to_excel(EXCEL, sheet_name="stocks", header=True, index=False)


def draw_pie():
    '''多支股票进行对比——饼图
    '''
    df = read_excel()       # 读取数据
    # 根据 振幅 列排序 ascending：默认True升序排列；False降序排列
    df = df.sort_values(by="振幅", axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last')
    print(df)
    print("股票根据【振幅】做过排序!")
    stock_names = df["股票名称"].tolist()
    stock_sum_values = [float(x.split("亿")[0]) for x in df["总市值"].tolist()]
    # 计算各数据占比
    data = [x / sum(stock_sum_values) for x in stock_sum_values]

    # 设置绘图的主题风格（不妨使用R中的ggplot分隔）
    plt.style.use('ggplot')
    explode = []
    for i in range(len(stock_names)):
        if i == 0:
            explode.append(0.1)         # 用于突出显示某一扇形,此时将前三位位凸显
        elif i == 1:
            explode.append(0.1)
        elif i == 2:
            explode.append(0.1)
        else:
            explode.append(0)
    # 颜色映射
    cmap = plt.cm.prism
    colors = cmap(np.linspace(0., 1., len(stock_names)))
    # 横纵坐标轴标准化处理，使饼图是正圆
    plt.axes(aspect='equal')
    # 控制x轴和y轴的范围
    plt.xlim(0, 6)
    plt.ylim(0, 6)
    # 自定义半径
    radius = 1          # 不小于1
    pctdistance = radius - 0.4
    labeldistance = radius + 0.1
    # 绘制饼图
    plt.pie(x=data,  # 绘图数据
            explode=explode,                    # 突出显示设置
            labels=stock_names,                 # 添加各扇形区域标签
            colors=colors,                      # 设置饼图的自定义填充色
            autopct='%.1f%%',                   # 设置百分比的格式，这里保留一位小数
            pctdistance=pctdistance,            # 设置百分比标签与圆心的距离
            labeldistance=labeldistance,        # 设置各扇形标签与圆心的距离
            startangle=180,                     # 设置饼图的初始角度
            radius=radius,                      # 设置饼图的半径
            counterclock=False,                 # 是否逆时针，这里设置为顺时针方向
            wedgeprops={'linewidth': 1, 'edgecolor': 'w'},          # 设置饼图内外边界的属性值
            textprops={'fontsize': 10, 'color': 'k'},               # 设置文本标签的属性值
            center=(1.8, 1.8),                  # 设置饼图的原点
            # frame=2                           # 是否显示饼图的图框，此处设置不显示
            )
    # 删除x轴和y轴的刻度
    plt.xticks(())
    plt.yticks(())
    # 添加图标题
    plt.title("多支股票总市值对比分布饼图")
    # 图例
    plt.legend(loc="lower left", fontsize=10, bbox_to_anchor=(-.3, .05))
    # 显示图形
    plt.show()


def draw_histogram():
    '''根据多支股票绘制【股票名称】——【最高】柱状图
    '''
    df = read_excel()       # 读取数据
    x = df["股票名称"]
    y = df["最高"]
    # 绘制折线图
    plt.bar(x, y, color='darkcyan', align='center')
    # 设置横坐标显示角度，角度是逆时针
    plt.xticks(rotation=-55)
    # 添加标题
    plt.title("股票可视化——柱状图")
    plt.ylabel("最高")
    plt.xlabel("股票名称")
    # 自动调整子图参数适应大小
    plt.tight_layout()
    # 图例
    plt.legend(["最高"], loc="upper right", fontsize=10)
    # 添加数值标签
    for x, y in enumerate(y):
        plt.text(x, y, '%s' % round(y, 1), ha='center')
    plt.show()


def draw_radar():
    '''根据多支股票绘制 最高、最低、今开、昨收、涨停、跌停 雷达图
    有实际意义，可对两支股票作对比
    '''
    df = read_excel()       # 读取数据
    print(df)
    print("请根据以上展示信息，输入两支股票索引进行对比！")
    print("例如：输入1，然后回车; 再输入2，然后回车; 即可对第2、3支股票进行对比。")
    num1 = int(input(">>>>>>>>>>【输入待展示的股票序号1】<<<<<<<<<\n"))
    num2 = int(input(">>>>>>>>>>【输入待展示的股票序号2】<<<<<<<<<\n"))
    # 选取 最高、最低、今开、昨收、涨停、跌停 这五列标题
    titles = df.columns.tolist()[2:8]
    # 股票一
    stock_name1 = df["股票名称"][num1]
    stock_code1 = df["股票代码"][num1]
    data1 = df.loc[num1].tolist()[2:8]      # 选取 最高、最低、今开、昨收、涨停、跌停 这六列数据
    # 股票二
    stock_name2 = df["股票名称"][num2]
    stock_code2 = df["股票代码"][num2]
    data2 = df.loc[num2].tolist()[2:8]      # 选取 最高、最低、今开、昨收、涨停、跌停 这六列数据
    data = [data1, data2]
    N = len(titles)     # 雷达图等分数目
    titles.append(titles[0])        # 标题数目和数据一致

    # 样式 大于当前的5
    sam = ['r-', 'm-', 'g-', 'b-', 'y-', 'k-', 'w-', 'c-']
    for i in range(len(data)):
        values = data[i]
        # 设置雷达图的角度，平分圆面
        angles = np.linspace(0, 2 * np.pi, N, endpoint=False)
        # 雷达图封闭 两种方法
        # values.append(values[0])
        values = np.concatenate((values, [values[0]]))
        # 角度
        angles = np.append(angles, angles[0])
        # 绘制折线图
        plt.polar(angles, values, sam[num1 % 5], lw=2)
        # 添加特征标签
        plt.thetagrids(angles * 180 / np.pi, titles)
        # 填充颜色
        plt.fill(angles, values, facecolor='c', alpha=0.4)
        # 标题
        plt.title('【' + stock_name1 + stock_code1 + '】 VS 【' + stock_name2 + stock_code2 + '】')
    plt.show()


if __name__ == '__main__':
    main()

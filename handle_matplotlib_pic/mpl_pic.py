'''
@Author: randolph
@Date: 2020-06-05 13:27:20
@LastEditors: randolph
@LastEditTime: 2020-06-10 12:25:15
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 【matplotlib作图三个题目】
希腊字母写法
https://www.cnblogs.com/gegemu/p/11459167.html
'''
import os
import os.path
import sys

import matplotlib.pyplot as plt
import numpy as np

# 支持中文
plt.rcParams['font.sans-serif'] = ['SimHei']    # 用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号


def pic_1():
    '''图一
    '''
    def f(t):
        '''阻尼正弦波计算公式
        '''
        s1 = np.cos(2 * np.pi * t)    # 余弦
        e1 = np.exp(-t)               # 自然数e的幂
        return s1 * e1 + 0.8

    def f2(t):
        return 0.5 * np.cos(t ** 2) + 0.8

    plt.xticks([np.pi / 3, np.pi * 2 / 3, np.pi, np.pi * 4 / 3, np.pi * 5 / 3],
               [r'$\pi/3$', r'$2\pi/3$', r'$\pi$', r'$4\pi/3$', r'$5\pi/3$'])
    t1 = np.arange(0, 5.0 * np.pi / 3, .001)      # 定义x轴(可以将步长改小，图像就很明显)
    # 曲线1 注意label的写法带有罗马字符
    l1 = plt.plot(t1, f(t1), color='red', linewidth=1, linestyle="-", label=r"exp$_\delta$ecay")
    # plt.setp(l1, markersize=3)                      # 设置点的大小
    # plt.setp(l1, markerfacecolor='C0')              # 颜色
    # 标题 横纵轴描述
    plt.title(u"阻尼衰减曲线")
    plt.xlabel("时间(s)")
    plt.ylabel("幅度(mV)")
    # 曲线2 注意label的写法带有幂
    l2 = plt.plot(t1, f2(t1), color='blue', linewidth=1, linestyle="--", label="cos($x^{2}$)")
    # 阴影区
    a, b = 0.8, 3
    xf = t1[np.where((t1 > a) & (t1 < b))]
    plt.fill_between(xf, f(xf), alpha=0.25)
    # plt.fill_between(xf,f(xf),f2(xf), alpha=0.25)     # 自定义阴影区
    # 图例位置
    plt.legend(loc='upper right')
    plt.show()


def pic_2():
    '''图二
    csv文件将header手动删除掉了
    XRD曲线图
    '''
    ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
    src_file = os.path.join(ROOT_PATH, "XRD_AFO.csv")           # 绝对路径拼接

    with open(src_file, 'r', encoding='utf-8') as data:
        ls = [x.split(',') for x in data]
        lsx = [float(x[0]) for x in ls]
        lsy = [float(x[1]) for x in ls]
        # 标题 横纵轴描述
        plt.title("XRD曲线图")
        plt.xlabel("Pstition（2-Theta）")
        plt.ylabel("Intensity")
        # 绘图
        plt.plot(lsx, lsy, color='red', linewidth=1)
        plt.show()


def pic_3():
    '''图三
    '''
    x = np.linspace(0, 2, 250)
    y = np.sin(np.pi * x * 2)
    plt.axhline(0, linestyle='-', color='black', linewidth=1)
    plt.plot(x, y, color='black', linewidth=1, linestyle='-')
    plt.axvspan(0, 0.5, 0.5, 1, color='green', alpha=0.5)
    plt.axvspan(1, 1.5, 0.5, 1, color='green', alpha=0.5)
    plt.axvspan(0.5, 1, 0, 0.5, color='red', alpha=0.5)
    plt.axvspan(1.5, 2, 0, 0.5, color='red', alpha=0.5)
    plt.show()


if __name__ == "__main__":
    pic_1()
    # pic_2()
    # pic_3()

'''
@Author: randolph
@Date: 2020-06-11 22:19:13
@LastEditors: randolph
@LastEditTime: 2020-06-12 11:11:48
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import numpy as np
import scipy.interpolate as itp
import matplotlib.pyplot as plt

date = range(0, 100, 10)

np.random.seed(0)       # 如果想得到固定的随机数，种子可以给相同的整数,注释掉这句则每次随机数都不同
number = 100 * np.random.normal(0, 1, len(date))        # 生成符合正态分布的随机数

x = np.array(range(0, 91))
y = itp.interp1d(date, number, kind="quadratic")        # 用 quadratic 插值(2阶B样条曲线插值)或者 cubic
y2 = y(x)
plt.plot(date, number, "*", x, y2)                      # 绘图
plt.show()

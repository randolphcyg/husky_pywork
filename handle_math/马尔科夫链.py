'''
@Author: randolph
@Date: 2020-07-08 11:31:06
@LastEditors: randolph
@LastEditTime: 2020-07-09 12:46:11
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 用python程序验证马尔科夫链形成过程
参考： https://blog.csdn.net/sinat_35821976/article/details/77094935
注意： 数据和函数是自己自定义的，注意根据自己情况作修改
'''
import numpy as np
import pylab as pl

p01 = np.array([0.5, 0.2, 0.3])
p02 = np.array([0.1, 0.4, 0.5])
p = np.array([[0.9, 0.075, 0.025], [0.13, 0.8, 0.07], [0.25, 0.25, 0.5]])
n = 30

c = ['r', 'g', 'b']                 # 颜色数组：红 绿 蓝


def draw(p0):
    for i in range(n):              # 遍历30次
        p0 = np.dot(p0, p)          # 点积
        for j in range(len(p)):     # 根据p长度决定画几条线(y轴)
            pl.scatter(i, p0[j], c=c[j], s=.5)          # 作图


pl.subplot(121)
draw(p01)           # 调用作图函数画p01
pl.subplot(122)
draw(p02)           # 调用作图函数画p02
pl.show()           # 显示绘图

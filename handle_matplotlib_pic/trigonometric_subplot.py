'''
@Author: randolph
@Date: 2020-06-11 22:47:59
@LastEditors: randolph
@LastEditTime: 2020-06-12 00:58:02
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
标注
https://blog.csdn.net/wizardforcel/article/details/54782628
'''
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']  # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False   # 用来正常显示负号
x = np.arange(0, 100)

# 获取x坐标
X = np.linspace(-np.pi, np.pi, 256, endpoint=True)
# 获取y坐标
sin, cos = np.sin(X), np.cos(X)

# 子图1 绘制正弦曲线
plt.subplot(221)
plt.plot(X, sin, "b-", lw=2.5, label="正弦")
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.set_title('正弦曲线')
plt.xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi],
           [r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
t = np.pi / 6  # 设定点x轴值
plt.scatter([t, ], [np.sin(t), ], 30, color='r')
plt.annotate(r'$\sin(\frac{\pi}{6})=\frac{1}{2}$',
             xy=(t, np.sin(t)),     # 点的位置
             xycoords='data',       # 注释文字的偏移量
             xytext=(50, 50),       # 文字离点的横纵距离
             textcoords='offset points',
             fontsize=13,  # 注释的大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.5"))       # 箭头指向的弯曲度
plt.plot([t, 0], [0.5, 0.5], color='r', linewidth=1, linestyle=":")                 # 作y轴垂线(t, 0.5)(0, 0.5)
plt.plot([t, t], [0.5, 0], color='r', linewidth=1, linestyle=":")                   # 作y轴垂线(t, 0.5)(t, 0)
plt.legend(loc='upper left')

# 子图2 不画
# plt.subplot(222)
# plt.plot(x, -x)

# 子图3 绘制余弦曲线
plt.subplot(223)
plt.plot(X, cos, "r-", lw=2.5, label="余弦")
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.set_title('余弦曲线')
plt.xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi],
           [r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
t = np.pi / 3  # 设定点x轴值
plt.scatter([t, ], [np.cos(t), ], 30, color='b')
plt.annotate(r'$\cos(\frac{\pi}{3})=\frac{1}{2}$',
             xy=(t, np.cos(t)),     # 点的位置
             xycoords='data',       # 注释文字的偏移量
             xytext=(25, 25),       # 文字离点的横纵距离
             textcoords='offset points',
             fontsize=13,           # 注释的大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.3"))       # 箭头指向的弯曲度
plt.plot([t, 0], [0.5, 0.5], color='b', linewidth=1, linestyle=":")                 # 作y轴垂线(t, 0.5)(0, 0.5)
plt.plot([t, t], [0.5, 0], color='b', linewidth=1, linestyle=":")                   # 作y轴垂线(t, 0.5)(t, 0)
plt.legend(loc='upper left')

# 子图4 绘制正切曲线
plt.subplot(224)
plt.plot(X, np.tan(X), "g", lw=2.5, label="正切")
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))
ax.set_title('正切曲线')
plt.xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi],
           [r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
plt.legend(loc='upper left')

plt.show()

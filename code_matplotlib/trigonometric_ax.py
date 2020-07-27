'''
@Author: randolph
@Date: 2020-06-12 00:00:08
@LastEditors: randolph
@LastEditTime: 2020-06-12 00:44:46
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import matplotlib.gridspec as gridspec
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']    # 用于正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False      # 用来正常显示负号
gs = gridspec.GridSpec(2, 2)                    # 将绘图区分成两行两列
ax1 = plt.subplot(gs[0, 0])                     # 指定ax1占用左上
ax2 = plt.subplot(gs[1, 0])                     # 指定ax2占用左下
ax3 = plt.subplot(gs[:, 1])                     # 指定ax3占用右边

x_data = np.linspace(-np.pi, np.pi, 64, endpoint=True)


# 1.绘制正弦曲线
ax1.plot(x_data, np.sin(x_data), color='r', label="正弦", linestyle=":")
# 设置刻度标记
ax1.set_xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi])
ax1.set_xticklabels([r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
ax1.spines['right'].set_color('none')
ax1.spines['top'].set_color('none')
ax1.spines['bottom'].set_position(('data', 0))
ax1.spines['left'].set_position(('data', 0))
t1 = np.pi / 6  # 设定点x轴值
ax1.scatter([t1, ], [np.sin(t1), ], 30, color='r')
ax1.annotate(r'$\sin(\frac{\pi}{6})=\frac{1}{2}$',
             xy=(t1, np.sin(t1)),   # 点的位置
             xycoords='data',       # 注释文字的偏移量
             xytext=(40, 40),       # 文字离点的横纵距离
             textcoords='offset points',
             fontsize=13,           # 注释的大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.6"))       # 箭头指向的弯曲度
ax1.plot([t1, 0], [0.5, 0.5], color='r', linewidth=1, linestyle=":")                # 作y轴垂线(t1, 0.5)(0, 0.5)
ax1.plot([t1, t1], [0.5, 0], color='r', linewidth=1, linestyle=":")                # 作y轴垂线(t1, 0.5)(t1, 0)
ax1.set_title('正弦曲线')
ax1.legend(loc='upper left')

# 2.绘制余弦曲线
ax2.plot(x_data, np.cos(x_data), color='b', label="余弦", linestyle=":")
# 设置刻度标记
ax2.set_xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi])
ax2.set_xticklabels([r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
ax2.spines['right'].set_color('none')
ax2.spines['top'].set_color('none')
ax2.spines['bottom'].set_position(('data', 0))
ax2.spines['left'].set_position(('data', 0))
# 画图注
t2 = np.pi / 3  # 设定点x轴值
ax2.scatter([t2, ], [np.cos(t2), ], 30, color='b')
ax2.annotate(r'$\cos(\frac{\pi}{3})=\frac{1}{2}$',
             xy=(t2, np.cos(t2)),   # 点的位置
             xycoords='data',       # 注释文字的偏移量
             xytext=(25, 25),       # 文字离点的横纵距离
             textcoords='offset points',
             fontsize=13,           # 注释的大小
             arrowprops=dict(arrowstyle="->", connectionstyle="arc3,rad=.3"))       # 箭头指向的弯曲度
ax2.plot([t2, 0], [0.5, 0.5], color='b', linewidth=1, linestyle=":")                # 作y轴垂线(t2, 0.5)(0, 0.5)
ax2.plot([t2, t2], [0.5, 0], color='b', linewidth=1, linestyle=":")                # 作y轴垂线(t2, 0.5)(t2, 0)
ax2.set_title('余弦曲线')
ax2.legend(loc='upper left')

# 4.绘制正切曲线
ax3.plot(x_data, np.tan(x_data), color='g', label="正切", linestyle=":")
ax3.set_xticks([-np.pi, -np.pi * 2 / 3, -np.pi / 3, np.pi / 3, np.pi * 2 / 3, np.pi])
ax3.set_xticklabels([r'-$\pi$', r'-$2\pi/3$', r'-$\pi/3$', r'$\pi/3$', r'$2\pi/3$', r'$\pi$'])
ax3.spines['right'].set_color('none')
ax3.spines['top'].set_color('none')
ax3.spines['bottom'].set_position(('data', 0))
ax3.spines['left'].set_position(('data', 0))
ax3.set_title('正切曲线')
ax3.legend(loc='upper left')

plt.show()

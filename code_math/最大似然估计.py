'''
@Author: randolph
@Date: 2020-07-08 14:42:59
@LastEditors: randolph
@LastEditTime: 2020-07-08 15:48:13
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
'''
import numpy as np
import pylab as pl

pl.rcParams['font.family'] = 'SimHei'


def fact(n):  # 求阶乘,建议使用递归方法
    if n == 0 or n == 1:
        return 1
    return (n * fact(n - 1))  # 2


def getp(n, k, p):  # 公式1或公式2 两个公式的通式，可以分别调用k或p。实现不同意义的计算概率函数值
    from scipy import stats
    return stats.binom.pmf(k, n, p)


n = 10  # n次伯努利试验
k = 6    # 正例为6个
y = [0] * (n + 1)  # 用于保存理论计算概率函数值
p = k / n  # 初步判断总体参数p最有可能最大概率
pl.subplot(121)
for i in range(n + 1):
    y[i] = getp(n, i, p)  # 4概率p固定，k的取值变化，根据式1，计算概率函数分布值
    pl.bar(i, y[i], color="r")  # k的取值变化的概率函数图

a, b = max(y), y.index(max(y))  # 5计算概率函数值y中最大值（b），和最大值的索引位置(a)。
pl.text(a, b, "k={1} p({1})={0}".format(str(a), str(b)))  # 6将y中最大值和最大值的索引位置在其位置上标出，输出拼凑的字符串。参考图1中内容。
pl.title("已知概率p=0.6,列举k次正例出现的概率")
pl.xlabel("k (1-10)")
pl.ylabel("p(x=k)")

pl.subplot(122)
p = np.linspace(0, 1, n + 1)
for i in range(n + 1):
    y[i] = getp(n, i, p)  # 7 k的取值固定,并取最大值时，概率p变化，根据式2，计算概率函数分布值
    pl.bar(i, y[i], color=["red", "green", "blue", "red", "green", "blue", "red", "green"])  # 8 p的取值变化的概率函数图
a, b = .6, .25  # 9计算概率函数值y中最大值（b），和最大值的索引位置(a)。
pl.text(a, b, "k={1} p({1})={0}".format(str(a), str(b)))  # 10将y中最大值和最大值的索引位置在其位置上标出，输出拼凑的字符串。参考图1中内容。
pl.legend(loc='upper left')
pl.title("已知实践概率k=6，n=10, 列举概率p正例出现的概率")
pl.xlabel("p (0-1)")
pl.ylabel("p(x=p)")
pl.show()

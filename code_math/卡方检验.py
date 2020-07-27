'''
@Author: randolph
@Date: 2020-07-07 16:31:45
@LastEditors: randolph
@LastEditTime: 2020-07-07 16:54:39
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion:
卡方检验或称x2检验，H0：两变量相互不独立（有关系，没区别，没差异，差异不显著），
针对的是分类变量，观察频数与期望频数没有差别。
实际观测值与理论推断值之间的偏离程度就决定卡方值的大小，
卡方值越大，越不符合，拒绝原假设；卡方值越小，偏差越小，越趋于符合，
若两个值完全相等时，卡方值就为0，表明理论值完全符合。
x2究竟要大到什么程度才能拒绝H0，可以查卡方分布表获得，也可借助卡方分布求出所对应的P值来确定。
如果P值很小，说明观察值与理论值偏离程度太大，应当拒绝无效假设，表示比较资料之间有显著差异。
'''
import numpy as np
from scipy.stats import chi2
data = np.array([[40, 55, 85], [10, 5, 5]])
rsum = np.sum(data, axis=1)
lsum = np.sum(data, axis=0)
e = np.zeros(data.shape)
print(e)
for i in range(e.shape[0]):
    for j in range(e.shape[1]):
        print(e[i][j])
        e[i][j] = ((data[i, j] - rsum[i] * lsum[j] / np.sum(data))**2) / (rsum[i] * lsum[j] / np.sum(data))
print(e)
x2 = np.sum(e)
print(x2)
df = (e.shape[0] - 1) * (e.shape[1] - 1)
print(df)
x2biao = chi2.isf(0.05, df)
print(x2biao)
if x2 > x2biao:
    print("refuse h0")
else:
    print("receive h0")

from scipy.stats import chi2_contingency
test = chi2_contingency(data)
print(test)

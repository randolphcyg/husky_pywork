'''
@Author: randolph
@Date: 2020-07-08 09:22:49
@LastEditors: randolph
@LastEditTime: 2020-07-08 10:44:58
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: python蒙特卡洛平均值法求定积分
'''
# import numpy as np

# point_list = np.linspace(0, 3, 10001)
# value = 0
# for i in range(10000):
#     x0 = point_list[i]
#     x1 = point_list[i + 1]
#     v = 0.5 * (x1 - x0) * (x0 / 25 + 0.2 + x1 / 25 + 0.2)
#     value += v


# print('p is :', value)


import time
from functools import wraps

import numpy as np


def func_timer(function):
    @wraps(function)
    def function_timer(*args, **kwargs):
        print('[Function: {name} 运行...]'.format(name=function.__name__))
        t0 = time.time()
        result = function(*args, **kwargs)
        t1 = time.time()
        print('[Function: {name} 结束, 耗时: {time:.2f}s]'.format(name=function.__name__, time=t1 - t0))
        return result
    return function_timer


def f(x):
    return x**2


@func_timer
def n(N):
    a = 1 / 3.0
    x = np.random.uniform(0, 1, N)  # 随机生成N个0-1之间的一维点
    c = f(x)  # 把x的值代入f（x）计算
    s = 0
    j = sum(c[::]) * 1.00 / N
    print("蒙特卡洛估计值为： ", j)
    print("与真实值之间的误差为：", abs(a - j))


n(100000)

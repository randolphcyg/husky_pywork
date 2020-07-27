'''
@Author: randolph
@Date: 2020-06-12 01:06:55
@LastEditors: randolph
@LastEditTime: 2020-06-12 12:24:24
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 项数不少于3的超越函数
'''
import numpy as np

import pandas as pd
import matplotlib.pyplot as plt
x = 4
num_list = np.linspace(0, 13, 500)
v = np.cos(num_list) + x**4 + x**3 + 198 + np.e**3 - np.log1p(x)      # 超越函数
ser = pd.Series(v, index=list(np.linspace(0, 13, 500)))
asd, as_2 = plt.subplots(figsize=(6, 6))
ser.plot(ax=as_2, grid=True, style='-', colormap='Blues_r')
plt.show()

# 实现一个超越函数：y = x*sin(x)
# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# ser = pd.Series(np.sin(np.linspace(0, 7, 1000)), index=list(np.linspace(0, 7, 1000)))
# asd, as_2 = plt.subplots(figsize=(6, 6))
# ser.plot(ax=as_2, grid=True, style='.', colormap='Blues_r')
# plt.show()

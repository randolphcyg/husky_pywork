import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

index = ['2020-07-16', '2020-07-17', '2020-07-20', '2020-07-21', '2020-07-22']
data_dict = {'price_close': [320.41, 321.9, 324.4, 325.69, 326.11],
             'change': [0, 1.49, 2.50, 1.29, 0.42]}

data_df = pd.DataFrame(data=data_dict, index=index)
print(data_df)
# print(data_df.index)
# 填price_close或者change就是收盘价或变化折线图
plt.plot(data_df.index.to_list(), data_df['price_close'], color='c', linewidth=1, linestyle=":")
plt.show()
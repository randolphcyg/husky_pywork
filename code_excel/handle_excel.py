'''
@Author: randolph
@Date: 2020-06-02 10:29:44
@LastEditors: randolph
@LastEditTime: 2020-06-02 12:43:15
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 处理俩表对比
'''
import pandas as pd

path1 = "F:\\Glacier\\DEM\\a1\\test\\pivo147034.xls"       # 表格1
path2 = "F:\\Glacier\\DEM\\a1\\test\\pivo148033.xls"       # 表格2
df1 = pd.read_excel(path1, encoding='utf-8', error_bad_lines=False)           # 读取源文件
cols = df1.columns.tolist()      # 取header
df2 = pd.read_excel(path2, encoding='utf-8', error_bad_lines=False)           # 读取源文件
# df1.fillna(0, inplace=True)       # 处理nan 貌似没啥用
# df2.fillna(0, inplace=True)


#先把所有的df1中的非Nan值替换成0
for i in range(1, 13):
    df1.loc[df1[int(i)].notnull(), int(i)] = 0

df1_list = df1.values.tolist()        # df数据框转list
df2_list = df2.values.tolist()        # df数据框转list

result = []
for i, (df1_line, df2_line) in enumerate(zip(df1_list, df2_list)):
    inside_list = []
    for j, (item1, item2) in enumerate(zip(df1_line, df2_line)):
        if not (item1 is None) and pd.isnull(item2):
            inside_list.append(item1)

        else:
            inside_list.append(float(item2))
    result.append(inside_list)
    result_df = pd.DataFrame(data=result)
    result_df.to_excel('F:\\Glacier\\DEM\\a1\\test\\result2.xls', header=cols, index=False)
print(result_df)

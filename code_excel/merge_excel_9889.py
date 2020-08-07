import os
import re

import numpy as np
import pandas as pd

FILE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
source = os.path.join(FILE_ROOT_PATH, '9889.xlsx')
output = os.path.join(FILE_ROOT_PATH, 'result_9889.xlsx')


def merge_sheets(path: str) -> pd.DataFrame:
    '''将每个表格的sheet页中日期、期货成交汇总、期货持仓汇总聚集到一起
    '''
    df = pd.read_excel(path, sheet_name=None)
    print(len(list(df.keys())))
    all_indexs = dict()
    all_sheet_df_res = pd.DataFrame()
    for sheet_index, sheet in enumerate(list(df.keys())):
        if sheet_index < len(list(df.keys())) + 1:     # 测试时候控制前几个
            print(sheet_index)
            df_sheet = pd.read_excel(path, sheet_name=sheet)
            row, col = df_sheet.shape
            child_indexs = []
            child_table1_flag = 0
            child_table2_flag = 0
            for r in range(row):
                each_row_list = list(df_sheet.loc[r])
                if "交易日期" in each_row_list:
                    key_date = str(each_row_list[7])
                    date_row = r
                    # print(key_date)
                elif "期货持仓汇总" in each_row_list:
                    # print(each_row_list)
                    # print("从此行开始截取数据", r)
                    first_start = r
                    child_indexs.append(first_start)
                    child_table1_flag = 1
                elif "合计" in each_row_list and child_table1_flag == 1:
                    # print(each_row_list)
                    # print("第一段结束", r)
                    first_end = r
                    child_indexs.append(first_end)
                    # 跳出前总结数据
                    if key_date:
                        all_indexs[key_date] = child_indexs
                elif "期权持仓汇总" in each_row_list:
                    # print(each_row_list)
                    # print("从此行开始截取数据", r)
                    second_start = r
                    child_indexs.append(second_start)
                    child_table2_flag = 1
                elif "合计" in each_row_list and child_table2_flag == 1:
                    # print(each_row_list)
                    # print("第二段结束", r)
                    second_end = r
                    if second_end not in child_indexs:
                        child_indexs.append(second_end)
                        # 跳出前总结数据
                        if key_date:
                            all_indexs[key_date] = child_indexs
            each_sheet_res = []     # 每个sheet页的结果
            # print(child_indexs)
            if len(child_indexs) == 2:
                df_sheet.loc[date_row][0] = df_sheet.loc[date_row][7]
                df_sheet.loc[date_row][1:] = np.nan
                each_sheet_res.append(df_sheet.loc[date_row])           # 日期行
                # print(df_sheet.loc[date_row][0])
                for i in range(child_indexs[0], child_indexs[1] + 1):
                    # print(i)
                    # print(df_sheet.loc[i])
                    each_sheet_res.append(df_sheet.loc[i])
            elif len(child_indexs) == 4:
                df_sheet.loc[date_row][0] = df_sheet.loc[date_row][7]
                df_sheet.loc[date_row][1:] = np.nan
                each_sheet_res.append(df_sheet.loc[date_row])           # 日期行
                # print(df_sheet.loc[date_row])
                for i in range(child_indexs[0], child_indexs[1] + 1):
                    # print(i)
                    # print(df_sheet.loc[i])
                    each_sheet_res.append(df_sheet.loc[i])
                for j in range(child_indexs[2], child_indexs[3] + 1):
                    # print(j)
                    # print(df_sheet.loc[j])
                    each_sheet_res.append(df_sheet.loc[j])
            # print(each_sheet_res)
            each_sheet_res_df = pd.DataFrame(each_sheet_res).reset_index(drop=True)
            all_sheet_df_res = pd.concat([all_sheet_df_res, each_sheet_res_df], axis=0)
        # break
    return all_sheet_df_res


if __name__ == "__main__":
    res = merge_sheets(source)
    res.to_excel(output, header=None, index=False)

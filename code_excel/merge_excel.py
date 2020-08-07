import os
import re

import numpy as np
import pandas as pd

FILE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
source = os.path.join(FILE_ROOT_PATH, '6666.xlsx')
output = os.path.join(FILE_ROOT_PATH, 'result_9999.xlsx')


def merge_sheets(path: str) -> pd.DataFrame:
    '''将每个表格的sheet页中日期、期货成交汇总、期货持仓汇总聚集到一起
    '''
    df = pd.read_excel(path, sheet_name=None)
    print(len(list(df.keys())))
    all_indexs = dict()
    all_sheet_df_res = pd.DataFrame()
    for sheet_index, sheet in enumerate(list(df.keys())):
        if sheet_index < len(list(df.keys())) + 1:     # 测试时候控制前几个，正常使用比长度大一即可，无意义
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
                elif "期货成交汇总" in each_row_list:
                    first_start = r
                    child_indexs.append(first_start)
                    child_table1_flag = 1
                elif "合计" in each_row_list and child_table1_flag == 1:
                    first_end = r
                    child_indexs.append(first_end)
                    # 跳出前总结数据
                    if key_date:
                        all_indexs[key_date] = child_indexs
                elif "期货持仓汇总" in each_row_list:
                    second_start = r
                    child_indexs.append(second_start)
                    child_table2_flag = 1
                elif "合计" in each_row_list and child_table2_flag == 1:
                    second_end = r
                    if second_end not in child_indexs:
                        child_indexs.append(second_end)
                        # 跳出前总结数据
                        if key_date:
                            all_indexs[key_date] = child_indexs
            each_sheet_res = []     # 每个sheet页的结果
            if len(child_indexs) == 2:
                df_sheet.loc[date_row][0] = df_sheet.loc[date_row][7]
                df_sheet.loc[date_row][1:] = np.nan
                each_sheet_res.append(df_sheet.loc[date_row])           # 日期行
                for i in range(child_indexs[0], child_indexs[1] + 1):
                    each_sheet_res.append(df_sheet.loc[i])
            elif len(child_indexs) == 4:
                df_sheet.loc[date_row][0] = df_sheet.loc[date_row][7]
                df_sheet.loc[date_row][1:] = np.nan
                each_sheet_res.append(df_sheet.loc[date_row])           # 日期行
                for i in range(child_indexs[0], child_indexs[1] + 1):
                    each_sheet_res.append(df_sheet.loc[i])
                for j in range(child_indexs[2], child_indexs[3] + 1):
                    each_sheet_res.append(df_sheet.loc[j])
            # print(each_sheet_res)
            each_sheet_res_df = pd.DataFrame(each_sheet_res).reset_index(drop=True)
            all_sheet_df_res = pd.concat([all_sheet_df_res, each_sheet_res_df], axis=0)
        # break
    return all_sheet_df_res


def modify_result(path: str) -> dict:
    '''修正结果，将每个文件的交易日期行只保留日期，然后统一到一行，然后再将各个表格数据汇总
    '''
    df_sheet = pd.read_excel(path, header=None)     # 无header，从第一行开始读
    row, col = df_sheet.shape
    print(row, col)
    date_indexs = []
    for r in range(row):
        each_row_list = list(df_sheet.loc[r])
        if bool(re.match(r'.*\d{4}-\d{2}-\d{2}.*', str(each_row_list[0]))):     # 正则匹配日期行
            date_indexs.append(r)
        else:
            pass

    each_day_dict = dict()
    for i, index in enumerate(date_indexs):
        if i + 1 < len(date_indexs):      # 每两条日期之间的数据
            data = df_sheet.loc[index:date_indexs[i + 1] - 1].reset_index(drop=True)
            each_day_dict[df_sheet.loc[index][0]] = data
            # break
        else:       # 最后一条数据
            data = df_sheet.loc[date_indexs[i]:].reset_index(drop=True)
            each_day_dict[df_sheet.loc[index][0]] = data
    return each_day_dict


def concat_dicts(A: pd.DataFrame, B: pd.DataFrame) -> pd.DataFrame:
    '''传入两df——A和B将其合并到C，先不同键值合并到C，然后同键值的作拼接
    '''
    def Merge(dict1, dict2):
        res = {**dict1, **dict2}
        return res
    C = Merge(A, B)

    for key, value in A.items():
        if key in C:
            # 相同键的合并：二表的时间行得删除drop下
            C[key] = pd.concat([C[key], value.drop(index=0)], axis=0).reset_index(drop=True)
        else:
            C[key] = value
    return C


def sort_dict_res(d: dict) -> dict:
    '''字典根据键值排序，日期小的往前排
    '''
    sorted_d = dict()
    for i in sorted(d):
        sorted_d[i] = d[i]
    return sorted_d


if __name__ == "__main__":
    # 步骤一 将每个表格的sheet页抽取合并，将步骤二注释掉，并修改每一个表格对应的路径；
    # 生成好结果表将步骤一注释掉，解开步骤二注释
    # res = merge_sheets(source)
    # res.to_excel(output, header=None, index=False)

    # 步骤二 合并整合表格，可以用modify_result检查方法挨个检查步骤一生成的表格，然后整体运行第二步出结果
    source_file_list = ['result_6666.xlsx',
                        'result_9088.xlsx',
                        'result_9889.xlsx',
                        'result_9999.xlsx']
    # 将步骤一的结果表送入修正方法
    output0 = os.path.join(FILE_ROOT_PATH, source_file_list[0])
    result_6666_dict = modify_result(output0)

    output1 = os.path.join(FILE_ROOT_PATH, source_file_list[1])
    result_9088_dict = modify_result(output1)

    output2 = os.path.join(FILE_ROOT_PATH, source_file_list[2])
    result_9889_dict = modify_result(output2)

    output3 = os.path.join(FILE_ROOT_PATH, source_file_list[3])
    result_9999_dict = modify_result(output3)
    
    # 将几个表格依次作拼接
    concat_res1 = concat_dicts(result_6666_dict, result_9088_dict)
    concat_res2 = concat_dicts(concat_res1, result_9889_dict)
    concat_res3 = concat_dicts(concat_res2, result_9999_dict)
    # 拼接字典结果排序
    sort_concat_res3 = sort_dict_res(concat_res3)
    # 结果字典转换为Dataframe结构并保存
    all_sheet_df_res = pd.DataFrame()
    for k, v in zip(sort_concat_res3.keys(), sort_concat_res3.values()):
        all_sheet_df_res = pd.concat([all_sheet_df_res, v], axis=0)

    all_res = os.path.join(FILE_ROOT_PATH, 'all_res.xlsx')
    all_sheet_df_res.to_excel(all_res, header=None, index=False)

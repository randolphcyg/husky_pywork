'''用来扫描java类中的api，统计所有的api
'''
import os
import re
import pandas as pd

# platform_path = r"E:\\randolph-zy\\公有云加解密\\srm-platform\\src\\main\\java\\org\\srm\\platform\\api\\controller\\v1\\"
# ROOT_PATH = os.path.dirname(platform_path)

supplier_path = r"E:\\randolph-zy\\公有云加解密\\srm-supplier\\src\\main\\java\\org\\srm\\supplier\\api\\controller\\v1\\"
ROOT_PATH = os.path.dirname(supplier_path)
all_files = os.listdir(ROOT_PATH)

FILE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(FILE_ROOT_PATH, 'controller_info.xlsx')


def scan(files):
    res = dict()
    for i, filename in enumerate(files):
        # print(filename)
        abs_file = os.path.join(ROOT_PATH, filename)
        # # print(i + 1 , abs_file)
        # print('{:.1f}%'.format(((i + 1) / len(all_files)) * 100), filename)       # 进度
        # 打开文件进行处理
        with open(abs_file, 'r', encoding='utf8') as rfile:  # 打开文件
            java_file = rfile.readlines()       # 读取全部内容
            clear_java_file_list = [x.strip() for x in java_file if x.strip() != '']       # 去换行符和空格
            # print(clear_java_file_list)
            url = []        # 每一个controller下的请求地址列表
            request = []    # 每一个controller下的请求类型列表
            for sen in clear_java_file_list:

                if bool(re.search(r'@RequestMapping', sen)):
                    # requestmapping = re.findall(r'@RequestMapping*', sen)
                    # print(sen)
                    local = re.findall(r'"(.*)"', sen)      # 匹配双引号之间的请求地址
                    if len(local) == 0:
                        print('该controller未能匹配请求地址！！！请人工复核')
                    else:
                        controller_request = str(local[0])
                        # print(controller_request)
                        # 第一列存储主要的controller请求地址
                # 搜索非主请求的
                if not bool(re.search(r'@RequestMapping', sen)):
                    if bool(re.search(r'@(.*)Mapping', sen)):
                        # print(sen)
                        local = re.findall(r'"(.*)"', sen)
                        # 第二列对应每个主controller的地址
                        # 第三列写请求类型
                        req_type = re.findall(r'@(.*)Mapping', sen)[0]

                        if len(local) == 0:
                            # print('此条直接用controller的')
                            url.append(controller_request)
                            request.append(req_type)
                            # print(controller_request, )
                            # print(req_type)
                        else:
                            url.append(controller_request + str(local[0]))
                            # print(controller_request + str(local[0]), )
                            # print(req_type)
                            request.append(req_type)
                        res[filename] = [url, request]
    # print(res)

    # 写入表格
    df = pd.read_excel(output)    # 读取源文件
    # print(df)
    for k, v in res.items():
        # print(k, v)
        for url, type in zip(v[0], v[1]):
            print(k, url, type)
        # print(v[0])
        # print(v[1])

        # break
        # a = pd.DataFrame(v)
        # print(a)


def read_file():
    is_exist = os.path.exists(output_file)
    if not is_exist:        # 校验表格存在性
        df = pd.DataFrame(columns=["controller",
                                   "url",
                                   "request",
                                   ])
        df.to_excel(output_file, encoding='utf-8', sheet_name="信息", index=False)
    df = pd.read_excel(output_file)    # 读取源文件
    print(df)


if __name__ == "__main__":
    scan(all_files)

    # 存储测试

    # row, col = df.shape
    # print(row, col)
    # nums_list = df.iloc[:, 0].values.tolist()

    # df.loc[row + 1] = ['test']
    # print(df)
    # pd.DataFrame(df).to_excel(output_file, sheet_name="信息", header=True, index=False)

'''用来扫描java类中的api，统计所有controller类文件中的api的url和请求类型
'''
import os
import re

import pandas as pd
controllers_root_path = r"E:\\randolph-zy\\公有云加解密\\srm-interface\\src\\main\\java\\org\\srm\\interfaces\\api\\controller\\v1\\"
# controllers_root_path = r"E:\\randolph-zy\\公有云加解密\\srm-platform\\src\\main\\java\\org\\srm\\platform\\api\\controller\\v1\\"

# controllers_root_path = r"E:\\randolph-zy\\公有云加解密\\srm-supplier\\src\\main\\java\\org\\srm\\supplier\\api\\controller\\v1\\"
sheet_name = controllers_root_path.split('\\')[6]       # sheet页命名是类似srm-supplier的服务名
header = ["controller", "url", "request", "对应菜单", "状态", "技术", "测试"]       # 表格头，除了前三项，后面均可改动
ROOT_PATH = os.path.dirname(controllers_root_path)
all_files = os.listdir(ROOT_PATH)       # 输入文件夹名称列表

FILE_ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output = os.path.join(FILE_ROOT_PATH, "公有云加解密.xlsx")      # 输出文件夹


def scan(files: list) -> dict:
    '''扫描该文件夹下所有controller类文件，整理出接口
    TODO:需要优化为只提供服务根目录文件夹路径，自动扫描所有层次文件夹中的controller
    返回值格式{'文件名': [[url1, url2, ...], [request1, ...]]}
    '''
    res = dict()
    for i, filename in enumerate(files):
        abs_file = os.path.join(ROOT_PATH, filename)
        # print(i + 1, abs_file)
        with open(abs_file, 'r', encoding='utf8') as rfile:  # 打开文件
            java_file = rfile.readlines()       # 读取全部内容
            controller_file_content_list = [x.strip() for x in java_file if x.strip() != '']       # 去换行符和空格
            url = []        # 每一个controller下的请求地址列表
            request = []    # 每一个controller下的请求类型列表
            for sen in controller_file_content_list:
                if bool(re.search(r'@RequestMapping', sen)):
                    request_mapping = re.findall(r'"(.*)"', sen)      # 匹配双引号之间的请求地址
                    if len(request_mapping) == 0:
                        print('该controller未能匹配请求地址！！！请人工复核')
                    else:
                        request_mapping_url = str(request_mapping[0])
                        # controller主请求RequestMapping
                # 搜索过滤每个请求的url
                if not bool(re.search(r'@RequestMapping', sen)):        # 过滤掉主请求
                    if bool(re.search(r'@(.*)Mapping', sen)):           # 包含注解@*Mapping的行
                        child_url = re.findall(r'"(.*)"', sen)
                        # 第二列 请求地址
                        req_type = re.findall(r'@(.*)Mapping', sen)[0]      # 请求类型
                        if len(child_url) == 0:     # 如果方法请求注解上没有子url，则直接写controller主请求RequestMapping
                            url.append(request_mapping_url)
                            request.append(req_type)
                        else:
                            url.append(request_mapping_url + str(child_url[0]))
                            request.append(req_type)
                        res[filename] = [url, request]
    return res


def read_file(path) -> pd.DataFrame:
    is_exist = os.path.exists(path)
    if not is_exist:        # 校验表格存在性
        df = pd.DataFrame(columns=header)
        # 新建文件并写表头
        df.to_excel(path, index=False)
    df = pd.read_excel(path)    # 读取源文件
    return df


def save_file(res_dict: dict, path: str = None) -> None:
    '''写入表格
    '''
    df = read_file(path)    # 打开目标文件
    for i, (k, v) in enumerate(res_dict.items()):
        for url, type in zip(v[0], v[1]):
            df.loc[i] = [k, url, type, None, None, '李静玲', None]
    print(df)
    # 检查是否已存在同名sheet页!!
    check_df = pd.read_excel(path, sheet_name=None)
    if sheet_name not in list(check_df.keys()):
        with pd.ExcelWriter(path, mode='a') as writer:
            df.to_excel(writer, sheet_name=sheet_name, index=False, columns=header)
        print("创建并写入sheet页成功,打开文档时注意sheet页.")
    else:
        print("已经存在同名sheet页!!")


if __name__ == "__main__":
    print("》》》新增sheet:" + sheet_name)
    res = scan(all_files)       # 扫描api
    save_file(res, output)      # 保存结果

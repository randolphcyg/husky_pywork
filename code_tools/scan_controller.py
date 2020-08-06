'''用来扫描java类中的api，统计所有的api
'''
import os
import re
import pandas as pd

platform_path = r"E:\\randolph-zy\\公有云加解密\\srm-platform\\src\\main\\java\\org\\srm\\platform\\api\\controller\\v1\\"
ROOT_PATH = os.path.dirname(platform_path)

all_files = os.listdir(ROOT_PATH)


def scan(files):
    for i, filename in enumerate(files):
        # print(filename)
        abs_file = os.path.join(ROOT_PATH, filename)
        # # print(i + 1 , abs_file)
        print('{:.1f}%'.format(((i + 1) / len(all_files)) * 100), filename)
        # 打开文件进行处理
        with open(abs_file, 'r', encoding='utf8') as rfile:  # 打开文件
            java_file = rfile.readlines()       # 读取全部内容
            clear_java_file_list = [x.strip() for x in java_file if x.strip() != '']       # 去换行符和空格
            # print(clear_java_file_list)
            for sen in clear_java_file_list:
                if bool(re.search(r'@RequestMapping', sen)):
                    # requestmapping = re.findall(r'@RequestMapping*', sen)
                    # print(sen)
                    local = re.findall(r'"(.*)"', sen)      # 匹配双引号之间的请求地址
                    if len(local) == 0:
                        print('该controller未能匹配请求地址！！！请人工复核')
                    else:
                        request = str(local[0])
                        print(request)
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
                            print(request, req_type)
                        else:
                            print(request + str(local[0]), req_type)
        # break


if __name__ == "__main__":
    scan(all_files)

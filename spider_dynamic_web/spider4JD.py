#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Author: randolph
@Date: 2020-06-04 10:42:52
@LastEditors: randolph
@LastEditTime: 2020-06-04 17:30:37
@version: 1.0
@Contact: cyg0504@outlook.com
@Descripttion: 网上找的比较固定，复用性较差的爬取京东页面的代码，修改了文件io和xpath定位元素的代码
没有改外层逻辑，需要优化地方很多，有时间再来看；
我认为可以结合jieba对某一些商品做一个评论的情感分析，这个应该不难
'''
import csv
import os
import time

import pandas as pd
import requests
from lxml import etree

ROOT_PATH = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(ROOT_PATH, 'JD_phone_info.xlsx')
# 定义函数抓取每页前30条商品信息


def crow_first(n):
    # 构造每一页的url变化
    url = 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&cid2=653&cid3=655&page=' + str(2 * n - 1)
    head = {'authority': 'search.jd.com',
            'method': 'GET',
            'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=4&s=84&scrolling=y&log_id=1529828108.22071&tpl=3_M&show_items=7651927,7367120,7056868,7419252,6001239,5934182,4554969,3893501,7421462,6577495,26480543553,7345757,4483120,6176077,6932795,7336429,5963066,5283387,25722468892,7425622,4768461',
            'scheme': 'https',
            'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
            'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
            }
    # print(url)
    r = requests.get(url, headers=head)
    r.encoding = 'utf-8'        # 指定编码方式，不然会出现乱码
    html1 = etree.HTML(r.text)
    # 定位到每一个商品标签li
    datas = html1.xpath('//li[contains(@class,"gl-item")]')
    df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
    for i, data in enumerate(datas):
        p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')[0]
        p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')[0]
        p_shop = data.xpath('div/div[@class="p-shop"]/span/a/text()')[0]
        comment_url = "https:" + data.xpath('div/div[@class="p-commit"]/strong/a/@href')[0]
        comments_list = item_comments(comment_url, head)
        # print(p_name, p_price, p_shop, comment_url, )
        df.loc[i * n] = [p_name, p_price, p_shop, comment_url, ]
        break
    pd.DataFrame(df).to_excel(output_file, sheet_name='京东信息', header=True, index=False)


# def crow_last(n):
#     # 获取当前的Unix时间戳，并且保留小数点后5位
#     a = time.time()
#     b = '%.5f' % a
#     url = 'https://search.jd.com/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=' + \
#         str(2 * n) + '&s=' + str(48 * n - 20) + '&scrolling=y&log_id=' + str(b)
#     head = {'authority': 'search.jd.com',
#             'method': 'GET',
#             'path': '/s_new.php?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA',
#             'scheme': 'https',
#             'referer': 'https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=%E6%89%8B%E6%9C%BA&cid2=653&cid3=655&page=3&s=58&click=0',
#             'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
#             'x-requested-with': 'XMLHttpRequest',
#             'Cookie': 'qrsc=3; pinId=RAGa4xMoVrs; xtest=1210.cf6b6759; ipLocation=%u5E7F%u4E1C; _jrda=5; TrackID=1aUdbc9HHS2MdEzabuYEyED1iDJaLWwBAfGBfyIHJZCLWKfWaB_KHKIMX9Vj9_2wUakxuSLAO9AFtB2U0SsAD-mXIh5rIfuDiSHSNhZcsJvg; shshshfpa=17943c91-d534-104f-a035-6e1719740bb6-1525571955; shshshfpb=2f200f7c5265e4af999b95b20d90e6618559f7251020a80ea1aee61500; cn=0; 3AB9D23F7A4B3C9B=QFOFIDQSIC7TZDQ7U4RPNYNFQN7S26SFCQQGTC3YU5UZQJZUBNPEXMX7O3R7SIRBTTJ72AXC4S3IJ46ESBLTNHD37U; ipLoc-djd=19-1607-3638-3638.608841570; __jdu=930036140; user-key=31a7628c-a9b2-44b0-8147-f10a9e597d6f; areaId=19; __jdv=122270672|direct|-|none|-|1529893590075; PCSYCityID=25; mt_xid=V2_52007VwsQU1xaVVoaSClUA2YLEAdbWk5YSk9MQAA0BBZOVQ0ADwNLGlUAZwQXVQpaAlkvShhcDHsCFU5eXENaGkIZWg5nAyJQbVhiWR9BGlUNZwoWYl1dVF0%3D; __jdc=122270672; shshshfp=72ec41b59960ea9a26956307465948f6; rkv=V0700; __jda=122270672.930036140.-.1529979524.1529984840.85; __jdb=122270672.1.930036140|85.1529984840; shshshsID=f797fbad20f4e576e9c30d1c381ecbb1_1_1529984840145'
#             }
#     r = requests.get(url, headers=head)
#     r.encoding = 'utf-8'
#     html1 = etree.HTML(r.text)
#     # 定位到每一个商品标签li
#     datas = html1.xpath('//li[contains(@class,"gl-item")]')
#     df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
#     for i, data in enumerate(datas):
#         p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')[0]
#         p_price = data.xpath('div/div[@class="p-price"]/strong/i/text()')[0]
#         comment_url = "https:" + data.xpath('div/div[@class="p-commit"]/strong/a/@href')[0]
#         comments_list = item_comments(comment_url, head)
#         # print(p_name, p_price, comment_url, )
#         df.loc[i * n * 2] = [p_name, p_price, comment_url, ]
#     pd.DataFrame(df).to_excel(output_file, sheet_name='京东信息', header=True, index=False)


def item_comments(url, head):
    '''商品评论页面
    '''
    print(url)
    item_comments_list = []
    req = requests.get(url, headers=head)
    req.encoding = 'utf-8'
    print(req.text)
    item_comments_html = etree.HTML(req.text)

    # 定位到每一个商品标签li
    item_comments_datas = item_comments_html.xpath('//div[contains(@class,"comment-item")]')
    print(item_comments_datas)
    # for i, data in enumerate(item_comments_datas):
    #     p_name = data.xpath('div/div[@class="p-name p-name-type-2"]/a/em/text()')[0]
    return item_comments_list


def analysis_JD_info():
    df = pd.read_excel(output_file, encoding='utf-8', error_bad_lines=False)    # 读取源文件
    mean_price = df.mean(axis=0)      # 手机均价
    print(mean_price)


if __name__ == '__main__':
    # 新建空表格文件
    is_exist = os.path.exists(output_file)
    if not is_exist:        # 校验表格存在性
        df = pd.DataFrame(columns=["商品名", "价格", "店铺", "评论地址"])       # 表格头
        df.to_excel(output_file, encoding='utf-8', sheet_name='京东信息', index=False)
    # 以下是源码设计，没来得急看为啥同功能写了两遍
    for i in range(1, 2):
        try:
            print('First_Page:' + str(i))
            crow_first(i)
        except Exception as e:
            print(e)

        # try:
        #     print('Last_Page:' + str(i))
        #     crow_last(i)
        # except Exception as e:
        #     print(e)
    # 分析
    # analysis_JD_info()

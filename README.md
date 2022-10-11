# husky_pywork

### 1.介绍
husky_pywork主要记录小的不需要长期迭代的项目，主要涉及`tkinter`、`matplotlib`、`pandas`数据处理内容, 另外还有django的待完善web;

### 2.软件架构

| 项目    | 描述                                    |
| ------- | --------------------------------------- |
| python3 | 主要编程语言                            |
| jieba   | 自然语言处理库(中文最好的处理工具)      |
| pandas  | 数据处理库 |
| numpy  | 数学库 |
| matplotlib  | 绘图库 |

### 3.安装教程

#### 3.1.[python环境配置](https://blog.csdn.net/qq_33997198/article/details/107420579)

#### 3.2.pipenv虚拟环境安装依赖：
全局安装pipenv
`pip install pipenv`
用pipenv的锁文件安装依赖
`pip install -p`                没有参数会自动寻找 Pipfile 文件
或者
`pip install -p Pipfile.lock`   根据 Pipfile.lock 安装指定依赖

```diff
- pip install -p
+ pip install -p Pipfile.lock
```

### 4.使用说明

| 模块                      | 描述                                                         |
| ------------------------- | ------------------------------------------------------------ |
| code_excel              | pandas处理表格的例子(原始文件未上传、需要安装pandas)         |
| poem                  | [用jieba和re分析唐诗三百首的小题目](https://blog.csdn.net/qq_33997198/article/details/106493983)(需要安装jieba库) |
| sims_tk             | [python3 tkinter和pandas完成学生信息管理系统(详解)](https://blog.csdn.net/qq_33997198/article/details/106535544) |
| code_txt                | 用来存放只对字符串和txt文件处理的代码                        |
| code_matplotlib     | [matplotlib作图实例](https://blog.csdn.net/qq_33997198/article/details/106663268) |
| django_html_demo/info_sys | [django应用——GP信息系统&校友录系统](https://blog.csdn.net/qq_33997198/article/details/107039610) |
| stock_spider | [python股票爬虫可视化](https://blog.csdn.net/qq_33997198/article/details/107325441) |
| sims_cmd | [python3学生信息管理系统-CMD版本](https://blog.csdn.net/qq_33997198/article/details/107181444) |

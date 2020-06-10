<!--
 * @Author: randolph
 * @Date: 2020-06-01 23:55:30
 * @LastEditors: randolph
 * @LastEditTime: 2020-06-10 12:49:49
 * @version: 1.0
 * @Contact: cyg0504@outlook.com
 * @Descripttion: 
--> 
# husky_pywork

### 1.介绍
用来记录自己与python学友共同完成的有意思的问题~

### 2.软件架构

| 项目    | 描述                                    |
| ------- | --------------------------------------- |
| python3 | 主要编程语言                            |
| jieba   | 自然语言处理库(中文最好的处理工具)      |
| pandas  | 代替python的原生文件读取包,提高处理效率 |

### 3.安装教程
#### 1.python3安装后，使用全局环境即可;
#### 2.需要配置pip的国内源
位置`C:\Users\<用户名>\AppData\Roaming\pip\`
下创建`pip.ini`文件，内容为
`[global] 
timeout = 6000 
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
[install]
trusted-host = https://pypi.tuna.tsinghua.edu.cn`
#### 3.打开cmd安装其他所需的三方库：
全局安装pipenv
`pip install pipenv`
用pipenv的锁文件安装依赖
`pip install -p`                没有参数会自动寻找 Pipfile 文件
或者
`pip install -p Pipfile.lock`   根据 Pipfile.lock 安装指定依赖

### 4.使用说明

| 模块                  | 描述                                                         |
| --------------------- | ------------------------------------------------------------ |
| handle_excel          | pandas处理表格的例子(原始文件未上传、需要安装pandas)         |
| poem_300              | [用jieba和re分析唐诗三百首的小题目](https://blog.csdn.net/qq_33997198/article/details/106493983)(需要安装jieba库) |
| handle_tk_gui         | [python3 tkinter和pandas完成学生信息管理系统(详解)](https://blog.csdn.net/qq_33997198/article/details/106535544) |
| handle_txt            | 用来存放只对字符串和txt文件处理的代码                        |
| handle_matplotlib_pic | [matplotlib作图实例](https://blog.csdn.net/qq_33997198/article/details/106663268) |
